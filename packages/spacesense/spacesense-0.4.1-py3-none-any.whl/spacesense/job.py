"""
Job.py
====================================
All classes necessary to use SpaceSense library for large datasets.
"""
import json
import logging
import os
from pathlib import Path

import grpc
import pandas as pd
from tqdm import tqdm

from spacesense import config
from spacesense.common.proto.backend import backend_pb2, backend_pb2_grpc
from spacesense.grpc_auth import GrpcAuth

logger = logging.getLogger(__name__)


class Job:
    """Class that allows you to interact with SpaceSense backend."""

    def __init__(
        self, name, workflow_id, experiment_id, status, id, backend_url=None, local_output_path=None, reason=None
    ):
        """Create an instance of the :py:class:`Job`

        Args:
            id (str, optional): Unique id of your compute instance. If not specified, automatically generates a unique ID
        """
        self.backend_url = backend_url or config.BACKEND_URL

        self.api_key = os.environ.get("SS_API_KEY")
        if not self.api_key:
            raise ValueError("Could not find SpaceSense API in SS_API_KEY environment variable.")
        self.id = id
        self.name = name
        self.workflow_id = workflow_id
        self.experiment_id = experiment_id
        self.status = status
        self.local_output_path = local_output_path
        self.reason = reason
        self._execution_report = None
        if self.experiment_id and not self.local_output_path:
            self.local_output_path = os.path.join("./generated", self.experiment_id)

    @classmethod
    def load_from_id(
        cls, experiment_id, id, backend_url=None, local_output_path=None, name=None, workflow_id=None, status=None
    ):
        job = cls(
            workflow_id=workflow_id,
            name=name,
            experiment_id=experiment_id,
            id=id,
            backend_url=backend_url,
            local_output_path=local_output_path,
            status=status,
        )
        job.refresh()
        return job

    def refresh(
        self,
    ):
        """Refresh the status of the current job and all it's tasks"""

        channel_opt = [
            ("grpc.max_send_message_length", config.GRPC_MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", config.GRPC_MAX_RECEIVE_MESSAGE_LENGTH),
        ]
        with grpc.secure_channel(
            self.backend_url,
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(config.CERT), grpc.metadata_call_credentials(GrpcAuth(self.api_key))
            ),
            options=channel_opt,
        ) as channel:
            stub = backend_pb2_grpc.JobStub(channel)
            request = backend_pb2.GetJobReportRequest(job_id=self.id, experiment_id=self.experiment_id)
            try:
                response = stub.GetJobReport(request)
                if response.status != backend_pb2.Status.Value("COMPLETED"):
                    self.status = "RUNNING"
                    logger.error(
                        "Could not find job status, if you just started this job, you should wait for some time for the job to start"
                    )
                    return
                self._execution_report = json.loads(response.execution_report)
                statuses = [status.get("status", "") for id, status in self._execution_report.items()]
                if "RUNNING" in statuses:
                    self.status = "RUNNING"
                elif "COMPLETED" not in statuses and "ERROR" in statuses:
                    self.status = "ERROR"
                elif "COMPLETED" in statuses:
                    self.status = "COMPLETED"
            except grpc.RpcError as e:
                logger.error(f"Could not refresh, try again .. detail : {e.details()}")

    def execution_report(self):
        return pd.DataFrame.from_dict(self._execution_report, orient="index")

    def download_result(self, output_dir=None):
        """get the status of the current Job and all the issued tasks"""

        channel_opt = [
            ("grpc.max_send_message_length", config.GRPC_MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", config.GRPC_MAX_RECEIVE_MESSAGE_LENGTH),
        ]
        with grpc.secure_channel(
            self.backend_url,
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(config.CERT), grpc.metadata_call_credentials(GrpcAuth(self.api_key))
            ),
            options=channel_opt,
        ) as channel:
            stub = backend_pb2_grpc.JobStub(channel)
            request = backend_pb2.StreamJobResultsRequest(job_id=self.id, experiment_id=self.experiment_id)
            try:
                self.local_output_path = output_dir or self.local_output_path
                Path(self.local_output_path).mkdir(parents=True, exist_ok=True)
                print(f"Starting to download Job results to path {self.local_output_path}")
                downloaded_list = []
                total_tasks = 0
                for response in tqdm(stub.StreamJobResults(request)):
                    total_tasks = response.total_tasks
                    if response.total_tasks == 0:
                        logger.info("No results found")
                    if response.current_task == 1:
                        logger.info("Downloading results")
                    with open(os.path.join(self.local_output_path, f"{response.task_id}.nc"), "wb") as f:
                        f.write(response.task_data)
                        downloaded_list.append(response.task_id)
                print(f"Downloaded {len(downloaded_list)} files out of {total_tasks}")
            except grpc.RpcError as e:
                logger.error(e.details())

    def retry(self):
        """get the status of the current Job and all the issued tasks"""

        # Allow to transfer up to 500mo as grpc message
        channel_opt = [
            ("grpc.max_send_message_length", config.GRPC_MAX_SEND_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", config.GRPC_MAX_RECEIVE_MESSAGE_LENGTH),
        ]
        with grpc.secure_channel(
            self.backend_url,
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(config.CERT), grpc.metadata_call_credentials(GrpcAuth(self.api_key))
            ),
            options=channel_opt,
        ) as channel:
            stub = backend_pb2_grpc.JobStub(channel)
            request = backend_pb2.RetryJobRequest(
                job_name=self.name,
                job_id=self.id,
                experiment_id=self.experiment_id,
                workflow_id=self.workflow_id,
            )
            try:
                response = stub.RetryJob(request)
                if response.status == backend_pb2.Status.Value("ERROR"):
                    self.status = "ERROR"
                    self.reason = response.reason
                    logger.error(f"Could not start to process this Job. reason: {self.reason}")
                elif response.status == backend_pb2.Status.Value("RUNNING"):
                    self.status = "RUNNING"
                    logger.info(f"Experiment (id:{response.experiment_id}) Started for Job(id:{response.job_id})")
            except grpc.RpcError as e:
                logger.error(e.details())

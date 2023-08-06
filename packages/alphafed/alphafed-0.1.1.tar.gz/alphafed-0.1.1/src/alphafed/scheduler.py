"""Algorithm scheduler."""


from abc import ABC, abstractmethod
from tempfile import TemporaryFile

import cloudpickle as pickle

from . import logger, task_logger
from .bass import BassProxy


class Scheduler(ABC):

    def launch_task(self, task_id: str):
        """Launch current task."""
        assert task_id and isinstance(task_id, str), f'invalid task ID: {task_id}'

        bass_proxy = BassProxy()
        with TemporaryFile() as tf:
            pickle.dump(self, tf)
            tf.seek(0)
            file_key = bass_proxy.upload_file(upload_name='model.pickle', fp=tf)
        bass_proxy.launch_task(task_id=task_id, pickle_file_key=file_key)

    def push_log(self, message: str):
        """Push a running log message to the task manager."""
        assert message and isinstance(message, str), f'invalid log message: {message}'
        if hasattr(self, 'task_id') and self.task_id:
            task_logger.info(message, extra={"task_id": self.task_id})
        else:
            logger.warn('Failed to push a message because context is not initialized.')

    @abstractmethod
    def _run(self, id: str, task_id: str, is_initiator: bool = False):
        """Run the scheduler.

        This function is used by the context manager, DO NOT modify it, otherwize
        there would be strange errors raised.

        :args
            :id
                the node id of the running context
            :task_id
                the id of the task to be scheduled
            :is_initiator
                is this scheduler the initiator of the task
        """

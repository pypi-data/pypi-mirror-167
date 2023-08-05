import importlib
import logging
import os

from django.apps import apps
from django.conf import settings

from aistudio_scheduler_lock.locks.database_advisory_lock import (
    DatabaseAdvisoryLock,
)
from aistudio_scheduler_lock.locks.database_lock import DatabaseLock
from aistudio_scheduler_lock.locks.file_lock import FCNTLFileLock

logger = logging.getLogger(__name__)


class SchedulerLockJob:
    # Am I owner of the lock
    lock_owner = False
    lock = None
    if settings.SCHEDULER_LOCK_TYPE == 'Database':
        lock = DatabaseLock(settings.SCHEDULER_LOCK_NAME, settings.SCHEDULER_LOCK_LEASE_TIME,
                            settings.SCHEDULER_LOCK_RECORD_ID)
    elif settings.SCHEDULER_LOCK_TYPE == 'Database_Advisory':
        lock = DatabaseAdvisoryLock(settings.SCHEDULER_LOCK_NAME,
                                    settings.SCHEDULER_LOCK_LEASE_TIME,
                                    settings.SCHEDULER_LOCK_RECORD_ID)
    elif settings.SCHEDULER_LOCK_TYPE == 'File':
        lock = FCNTLFileLock(os.path.join(settings.LOCK_FILE_BASE_PATH, "aistudio.lock"))
    else:
        raise Exception(f"Scheduler lock type {settings.SCHEDULER_LOCK_TYPE} not supported.")

    jobs = []

    @staticmethod
    def get_schedules_master():
        schedules_class_str = settings.SCHEDULES_MASTER_CLASS
        schedules_class_listified = schedules_class_str.split('.')
        module_name = '.'.join(schedules_class_listified[:-1])
        class_name = schedules_class_listified[-1]

        module = importlib.import_module(module_name)

        return getattr(module, class_name)

    @classmethod
    def scheduler_lock(cls) -> None:
        logger.debug(f"running scheduler_lock job, pid: {os.getpid()}, jobs: {cls.jobs}")

        scheduler_lock_app = apps.get_app_config('aistudio_scheduler_lock')
        if cls.lock_owner:
            if not cls.lock.renew_lease():
                for j in cls.jobs:
                    logger.debug(f"removing jobs: process {os.getpid()}, removed jobid: {j.id}")

                    try:
                        scheduler_lock_app.scheduler.remove_job(j.id)
                    except Exception as e:
                        logger.exception(e)
                    else:
                        logger.debug(f"removed job: process {os.getpid()}, removed jobid: {j.id}")
                cls.lock_owner = False
                cls.jobs = []

        elif cls.lock.try_acquire_lock():
            logger.debug(f"VOILA I {os.getpid()} am the lock owner VOILA")
            cls.lock_owner = True
            SchedulesMaster = cls.get_schedules_master()
            for mj in SchedulesMaster.get_all():
                # j = scheduler_lock_app.scheduler.add_job(mj[0], mj[1], seconds=mj[2], name=mj[3])
                j = scheduler_lock_app.scheduler.add_job(**mj)

                logger.debug(f"adding jobs: {os.getpid()} added jobid: {j.id}")
                cls.jobs.append(j)

    @classmethod
    def can_execute_task(cls) -> bool:
        return cls.lock.can_execute_task()

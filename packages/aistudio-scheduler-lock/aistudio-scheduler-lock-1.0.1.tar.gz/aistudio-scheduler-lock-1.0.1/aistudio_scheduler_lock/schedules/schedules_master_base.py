from abc import ABC, abstractmethod
from typing import TypedDict


class SchedulesDict(TypedDict):
    func: callable
    trigger: str
    seconds: int
    name: str


class SchedulesMasterBase(ABC):

    @abstractmethod
    def get_all(self) -> SchedulesDict:
        raise NotImplementedError()

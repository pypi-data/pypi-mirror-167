# -*- coding: utf-8 -*-
from functools import total_ordering
from typing import List, Set

from . import AbstractJob, BatchJob, TimeInterval


class AbstractJobSchedule(object):
    """
    An abstract entity representing the resulting job schedule.
    """

    def __init__(self, job: AbstractJob, execution_intervals: List[TimeInterval]) -> None:
        """
        Initialize the class with parameters.
        :param job: Job that the schedule was created for.
        :param execution_intervals: Scheduled time of the job.
        """
        self.job = job
        self.execution_intervals = execution_intervals

    @property
    def duration(self) -> int:
        return sum(time_interval.duration for time_interval in self.execution_intervals)


class JobScheduleMI(AbstractJobSchedule):
    """
    Job schedule that might have more than one execution window. MI stands for multiple intervals.
    """

    def __str__(self) -> str:
        return "JobScheduleMI(job={0}, execution_intervals={1})".format(
            self.job,
            self.execution_intervals
        )

    __repr__ = __str__


@total_ordering
class JobSchedule(JobScheduleMI):
    """
    Job schedule with a single execution window.
    """

    def __init__(
            self,
            job: AbstractJob,
            execution_start: int,
            execution_end: int,
    ) -> None:
        """
        Initialize the class with parameters.
        :param job: Job that the schedule was created for.
        :param execution_start: Start of the execution window.
        :param execution_end: End of the execution window.
        """
        super(JobSchedule, self).__init__(job, [TimeInterval(execution_start, execution_end)])

    @property
    def execution_start(self) -> int:
        return self.execution_intervals[0].start

    @execution_start.setter
    def execution_start(self, execution_start: int) -> None:
        self.execution_intervals[0].start = execution_start

    @property
    def execution_end(self) -> int:
        return self.execution_intervals[0].end

    @execution_end.setter
    def execution_end(self, execution_end: int) -> None:
        self.execution_intervals[0].end = execution_end

    def __str__(self) -> str:
        return "JobSchedule(job={0}, execution_start={1}, execution_end={2})".format(
            self.job,
            self.execution_start,
            self.execution_end,
        )

    __repr__ = __str__

    def __eq__(self, other: 'JobSchedule') -> bool:
        return (self.execution_start, self.execution_end) == (other.execution_start, other.execution_end)

    def __lt__(self, other: 'JobSchedule') -> bool:
        return (self.execution_start, self.execution_end) < (other.execution_start, other.execution_end)

    def __hash__(self) -> int:
        return self.job.id


@total_ordering
class BatchJobSchedule(object):
    """
    Schedule of a single batch.
    """

    def __init__(self, jobs: Set[BatchJob], execution_start: int, execution_end: int) -> None:
        """
        Initialize the class with parameters.
        :param jobs: Jobs in the batch.
        :param execution_start: Start of the execution window for the batch.
        :param execution_end: End of the execution window for the batch.
        """
        self.jobs = jobs
        self.execution_start = execution_start
        self.execution_end = execution_end

    @property
    def size(self) -> int:
        return len(self.jobs)

    def __str__(self) -> str:
        return "Batch(jobs={0}, execution_start={1}, execution_end={2})".format(
            self.jobs,
            self.execution_start,
            self.execution_end,
        )

    __repr__ = __str__

    def __eq__(self, other: 'BatchJobSchedule') -> bool:
        return (self.execution_start, -len(self.jobs)) == (other.execution_start, -len(other.jobs))

    def __lt__(self, other: 'BatchJobSchedule') -> bool:
        return (self.execution_start, -len(self.jobs)) < (other.execution_start, -len(other.jobs))

# python3

# AssignedJob = namedtuple("AssignedJob", ["worker_id", "finish_time"])


class Thread:
    def __init__(self, idx, job_time):
        self.worker_id = idx
        self.finish_time = job_time


class ParallelProcces:
    """_summary_"""

    def __init__(self, n_workers):
        self.result = []
        self.num_workers = n_workers
        self.workers = [Thread(i, 0) for i in range(self.num_workers)]

    def _get_minichld(self, idx):
        left_child = idx * 2 + 1
        right_child = idx * 2 + 2
        if right_child + 1 > self.num_workers:
            return left_child
        elif (
            self.workers[left_child].finish_time
            == self.workers[right_child].finish_time
        ):
            if self.workers[left_child].worker_id < self.workers[right_child].worker_id:
                return left_child
            else:
                return right_child
        elif (
            self.workers[left_child].finish_time < self.workers[right_child].finish_time
        ):
            return left_child
        else:
            return right_child

    def arrange(self, idx=0):
        # Arrange code
        while idx * 2 + 2 <= self.num_workers:
            mc = self._get_minichld(idx)
            if self.workers[mc].finish_time < self.workers[idx].finish_time:
                self.workers[mc], self.workers[idx] = (
                    self.workers[idx],
                    self.workers[mc],
                )
            if self.workers[mc].finish_time == self.workers[idx].finish_time:
                if self.workers[mc].worker_id < self.workers[idx].worker_id:
                    self.workers[mc], self.workers[idx] = (
                        self.workers[idx],
                        self.workers[mc],
                    )

            idx = mc

    def assign_jobs(self, jobs):
        # Main code
        for job_ in jobs:
            active_worker = self.workers[0]
            self.result.append((active_worker.worker_id, active_worker.finish_time))
            active_worker.finish_time += job_
            self.arrange()
        return self.result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    thread_machine = ParallelProcces(n_workers)
    assigned_jobs = thread_machine.assign_jobs(jobs)

    for worker_id, job in assigned_jobs:
        print(worker_id, job)


if __name__ == "__main__":
    main()

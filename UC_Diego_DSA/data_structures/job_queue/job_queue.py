# python3
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker_id", "started_at"])


def assign_jobs(n_workers, jobs):
    workers = [AssignedJob(i, 0) for i in range(5)]
    result = []

    def arrange(idx=0):
        def minichld(idx):
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            if right_child > n_workers:
                return left_child
            elif workers[left_child].started_at == workers[
                    right_child].started_at:
                if workers[left_child].worker_id < workers[
                        right_child].worker_id:
                    return left_child
                else:
                    return right_child
            elif workers[left_child].started_at < workers[
                    right_child].started_at:
                return left_child
            else:
                return right_child

        # arange code
        while idx * 2 + 1 <= n_workers:
            mc = minichld(idx)
            if workers[mc].started_at < workers[idx].started_at:
                workers[mc], workers[idx] = workers[mc], workers[idx]
            idx = mc

    #main code
    for job in jobs:
		active_worker = workers[0]
		result.append(active_worker)
        next_free_time[next_worker] += job
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker_id, job.started_at)


if __name__ == "__main__":
    main()

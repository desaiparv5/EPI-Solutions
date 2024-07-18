import collections


PairedTask = collections.namedtuple("PairedTask", ("task1", "task2"))


def optimum_task_assignment(tasks):
    tasks.sort()
    return [
        PairedTask(tasks[i], tasks[~i])
        for i in range(len(tasks)//2)
    ]


def main():
    print(optimum_task_assignment([5,1,8,9]))


if __name__ == "__main__":
    main()

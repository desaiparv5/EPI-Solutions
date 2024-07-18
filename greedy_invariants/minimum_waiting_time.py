def minimum_waiting_time(queries):
    queries.sort()
    wait_time = 0
    for ind, val in enumerate(queries):
        reamining_queries = len(queries) - ind - 1
        wait_time += reamining_queries*val
    return wait_time


def main():
    print(minimum_waiting_time([2,5,1,3]))


if __name__ == "__main__":
    main()

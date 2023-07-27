"""If we can reach the end of array of steps"""
from time import process_time_ns


def can_reach_end(arr):
    end = 0
    for ind, val in enumerate(arr):
        if end < ind:
            break
        end = max(end, (ind + val) if val else 0)
    return end >= len(arr) - 1


def num_steps_to_reach_end(arr):
    if not arr: return -1
    if len(arr) == 1: return 0
    if not arr[0]: return -1

    min_jump_arr = [float("inf") for _ in arr]
    min_jump_arr[-1] = 0

    for ind in range(len(arr)-2, -1, -1):
        if arr[ind] == 0:
            min_jump_arr[ind] = float("inf")
            continue
        elif arr[ind] >= (len(arr) - 1):
            min_jump_arr[ind] = 1
            continue
        else:
            min_jump_arr[ind] = 1 + min(min_jump_arr[ind+1 : ind+arr[ind]+1])
    return -1 if min_jump_arr[0] == float("inf") else min_jump_arr[0]


def main():
    arr = [4, 1, 0]
    start_time = process_time_ns()
    print(can_reach_end(arr))
    print(f"Time taken: {process_time_ns() - start_time}")

    start_time = process_time_ns()
    print(num_steps_to_reach_end(arr))
    print(f"Time taken: {process_time_ns() - start_time}")


if __name__ == "__main__":
    main()

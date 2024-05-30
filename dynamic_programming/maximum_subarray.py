import itertools


def maximum_subarray(nums):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(nums):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum


def main():
    print(maximum_subarray([5,4,-1,7,8]))

if __name__ == "__main__":
    main()

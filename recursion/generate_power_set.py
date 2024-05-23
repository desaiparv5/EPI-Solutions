from typing import List


def generate_power_set(nums: List[int]) -> List[List[int]]:
    return [[nums[i] for i in range(len(nums)) if j & 1 << i] for j in range(2**len(nums))]


def generate_power_set_recursive(nums: List[int]) -> List[List[int]]:
    res = []
    def helper(curr_index, curr_set):
        if curr_index == len(nums):
            res.append(curr_set.copy())
            return
        helper(curr_index + 1, curr_set + [nums[curr_index]])
        helper(curr_index + 1, curr_set)
    helper(0, [])
    return res


def generate_power_set_w_duplicates(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    res = []
    def helper(curr_index, curr_set):
        if curr_index == len(nums):
            res.append(curr_set.copy())
            return
        helper(curr_index + 1, curr_set + [nums[curr_index]])
        while curr_index + 1 < len(nums) and nums[curr_index + 1] == nums[curr_index]:
            curr_index += 1
        helper(curr_index + 1, curr_set)
    helper(0, [])
    return res

def main():
    print(generate_power_set([1,2,3,4]))
    print(generate_power_set_recursive([1,2,3,4]))
    print(generate_power_set_w_duplicates([1,2,2,4]))


if __name__ == "__main__":
    main()

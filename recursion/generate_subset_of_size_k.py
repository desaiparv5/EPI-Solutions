from typing import List


def generate_subsets_size_k(nums: List[int], k) -> List[List[int]]:
    res = []
    def helper(offset, curr_set):
        if offset == len(nums) and len(curr_set) != k:
            return
        if len(curr_set) == k:
            res.append(curr_set.copy())
            return
        helper(offset + 1, curr_set)        
        helper(offset + 1, curr_set + [nums[offset]])        
    helper(0, [])
    return res

def main():
    print(generate_subsets_size_k([1,2,3,4,5], 2))


if __name__ == "__main__":
    main()

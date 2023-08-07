from typing import Any
from merge_sorted_files import merge_sorted_arrays
import itertools


def sort_increasing_decreasing_array(array):
    class Monotonic:
        def __init__(self):
            self._last = float("-inf")
        
        def __call__(self, curr) -> Any:
            res = curr < self._last
            self._last = curr
            return res
    return merge_sorted_arrays([list(group)[::-1 if is_decreasing else 1] for is_decreasing, group in itertools.groupby(array, Monotonic())])


def main():
    array = [1,22,25,11,10,7,6,68,75,77,90,99,101,102]
    array = sort_increasing_decreasing_array(array)
    print(array)


if __name__ == "__main__":
    main()

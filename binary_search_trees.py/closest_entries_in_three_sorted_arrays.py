from typing import List


def closest_entries_in_three_sorted_arrays(array1: List[int], array2, array3) -> List[int]:
    p, q, r = len(array1), len(array2), len(array3)
    res1, res2, res3 = 0, 0, 0
    i, j, k = 0, 0, 0
    curr_diff = float("inf")
    while i < p and j < q and k < r:
        minimum = min(array1[i], array2[j], array3[k])
        maximum = max(array1[i], array2[j], array3[k])

        if (maximum - minimum) < curr_diff:
            curr_diff = maximum - minimum
            res1, res2, res3 = i, j, k
        if minimum == array1[i]:
            i += 1
        elif minimum == array2[j]:
            j += 1
        else:
            k += 1
    return [array1[res1], array2[res2], array3[res3]]


def main():
    array1 = [5, 10, 15]
    array2 = [3, 6, 9, 12, 15]
    array3 = [8, 16, 24]
    print(closest_entries_in_three_sorted_arrays(array1, array2, array3))


if __name__ == "__main__":
    main()

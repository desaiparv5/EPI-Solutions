from collections import namedtuple

SubArray = namedtuple("SubArray", ["start", "end"])


def smallest_sequentially_covering_subset(text, substring):
    substring_idx = {val: ind for ind, val in enumerate(substring)}
    latest_occurance = [-1] * len(substring)
    shortest_subarray_length = [float("inf")] * len(substring)
    shortest_length = float("inf")
    result = SubArray(-1, -1)
    for ind, char in enumerate(text):
        if char in substring_idx:
            substr_idx = substring_idx[char]
            if substr_idx == 0:
                shortest_subarray_length[substr_idx] = 1
            elif shortest_subarray_length[substr_idx - 1] != float("inf"):
                distance_to_prev_keyword = ind - latest_occurance[substr_idx - 1]
                shortest_subarray_length[substr_idx] = distance_to_prev_keyword + shortest_subarray_length[substr_idx - 1]
            latest_occurance[substr_idx] = ind

            if substr_idx == len(substring) - 1 and shortest_subarray_length[-1] < shortest_length:
                shortest_length = shortest_subarray_length[-1]
                result = (ind - shortest_length + 1, ind)
    return result


def main():
    text = "abdcdebdde"
    substring = "cd"
    print(smallest_sequentially_covering_subset(text, substring))


if __name__ == "__main__":
    main()

def longest_subarray_distinct_entries(string):
    most_recent_occurance = {}
    subarray_start = 0
    max_subarray_length = 0
    for ind, char in enumerate(string):
        if char in most_recent_occurance:
            char_idx = most_recent_occurance[char]
            if char_idx >= subarray_start:
                max_subarray_length = max(ind - subarray_start, max_subarray_length)
                subarray_start = char_idx + 1
        most_recent_occurance[char] = ind        
    return max_subarray_length


def main():
    string = "fsfetwenwe"
    print(longest_subarray_distinct_entries(string))


if __name__ == "__main__":
    main()

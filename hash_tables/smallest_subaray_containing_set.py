from collections import defaultdict, Counter


def smallest_subarray_containing_set(text, substring):
    need = Counter(substring)
    have = defaultdict(int)
    num_matches, left = 0, 0
    min_window_size = float("inf")
    min_window = ""
    for right in range(len(text)):
        char = text[right]
        if char in need:
            have[char] += 1
            if have[char] <= need[char]:
                num_matches += 1
            while num_matches == len(substring) and left <= right:
                if num_matches == len(substring):
                    if min_window_size > (right - left + 1):
                        min_window_size = right - left + 1
                        min_window = text[left:right + 1]
                rem_char = text[left]
                if have[rem_char] and have[rem_char] == need[rem_char]:
                    num_matches -= 1
                have[rem_char] -= 1
                left += 1
    return min_window


def main():
    text = "ADOBECODEBANC"
    substring = "ABC"
    print(smallest_subarray_containing_set(text, substring))


if __name__ == "__main__":
    main()

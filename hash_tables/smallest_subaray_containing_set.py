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


def smallest_subarray_containing_all_elements(text):
    substring = set(text)
    return smallest_subarray_containing_set(text, substring)


def rearrange_text_for_max_substring_of_distinct_chars(text):
    frequency_count = Counter(text)
    ordered_text = ""
    while len(frequency_count) > 1:
        char, freq = frequency_count.most_common(1)[0]
        ordered_text += char * freq
        frequency_count.pop(char)
    char, freq = frequency_count.most_common(1)[0]
    ordered_text = char * freq + ordered_text
    return ordered_text


def rearrange_letters_equidistant(text, k):
    char_freq = Counter(text)
    ordered_text = [None] * len(text)
    filled_index = 0
    while char_freq:
        char, freq = char_freq.most_common(1)[0]
        curr_index = filled_index
        for _ in range(freq):
            ordered_text[curr_index] = char
            curr_index += k
        char_freq.pop(char)
        filled_index += 1
        if filled_index < len(text) - 1 and ordered_text[filled_index]:
            while ordered_text[filled_index]:
                filled_index += 1
    return "".join(char for char in ordered_text if char)


def main():
    text = "ADOBECODEBANC"
    substring = "ABC"
    print(smallest_subarray_containing_set(text, substring))
    print(smallest_subarray_containing_all_elements(text))
    print(rearrange_text_for_max_substring_of_distinct_chars(text))
    print(rearrange_letters_equidistant(text, 3))


if __name__ == "__main__":
    main()

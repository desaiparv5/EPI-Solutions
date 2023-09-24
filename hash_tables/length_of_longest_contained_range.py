def longest_contained_range(array):
    unique_entries = set(array)
    max_range = 0
    while unique_entries:
        a = unique_entries.pop()
        lower_bound = a - 1
        while lower_bound in unique_entries:
            lower_bound -= 1
        upper_bound = a + 1
        while upper_bound in unique_entries:
            upper_bound += 1
        max_range = max(max_range, upper_bound - lower_bound - 1)

    return max_range


def main():
    array = [10, 5, 3, 11, 6, 100, 4]
    print(longest_contained_range(array))


if __name__ == "__main__":
    main()

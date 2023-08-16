def search_element_equal_to_its_index(array):
    # Given: array is sorted.
    def _helper(low, high):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        difference = array[mid] - mid
        if difference == 0:
            return mid
        if difference > 0:
            return _helper(low, mid - 1)
        return _helper(mid + 1, high)
    return _helper(0, len(array) - 1)


def main():
    array = [-4, -1, 0, 3, 9, 10]
    print(search_element_equal_to_its_index(array))


if __name__ == "__main__":
    main()

def first_occurrance(array, element):
    left, right, result = 0, len(array) - 1, -1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == element:
            result = mid
            right = mid - 1
        elif array[mid] > element:
            right = mid - 1
        else:
            left = mid + 1

    return result


def last_occurrance(array, element):
    left, right, result = 0, len(array) - 1, -1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == element:
            result = mid
            left = mid + 1
        elif array[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    return result


def first_greater_occurrance(array, element):
    last_index = last_occurrance(array, element)
    if last_index == len(array) - 1:
        return -1
    return last_index + 1


def find_local_minima(array):
    def local_minima_helper(low, high):
        if low > high:
            return -1
        mid = low - (high - low) // 2
        if (mid == 0 or array[mid] < array[mid - 1]) and (mid == len(array)-1 or array[mid] < array[mid + 1]):
            return mid
        elif mid > 0 and array[mid] > array[mid - 1]:
            return local_minima_helper(mid + 1, high)
        return local_minima_helper(low, mid - 1)

    return local_minima_helper(0, len(array) - 1)


def find_enclosing_interval(array, element):
    return [first_occurrance(array, element), last_occurrance(array, element)]


def is_prefix_in_strings(array, prefix):
    def _helper(low, high):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if array[mid].startswith(prefix):
            return mid
        elif array[mid][0:len(prefix)] < prefix:
            return _helper(mid + 1, high)
        return _helper(low, mid - 1)
    return _helper(0, len(array) - 1)


def main():
    array = [1,3,3,3,3,3,4]
    element = 3
    print(first_occurrance(array, element))
    print(first_greater_occurrance(array, element))


if __name__ == "__main__":
    main()

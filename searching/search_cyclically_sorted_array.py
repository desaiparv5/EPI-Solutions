# Given all elements are distinct
def search_smallest_in_cyclically_sorted_array(array):
    def _helper(low, high):
        if low == high:
            return low
        mid = low + (high - low) // 2
        if array[mid] > array[high]:
            low = mid + 1
        else:
            high = mid
        return _helper(low, high)
    return _helper(0, len(array) - 1)


def search_max_in_asc_desc_array(array):
    def _helper(low, high):
        if low == high:
            return low
        mid = low + (high - low) // 2
        if array[mid] > array[mid+1] and array[mid] > array[mid-1]:
            return mid
        elif array[mid+1] > array[mid]:
            return _helper(mid + 1, high)
        return _helper(low, mid - 1)
    return _helper(0, len(array) - 1)


def search_element_in_cyclically_sorted_array(array, element):
    def _helper(low, high):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if array[mid] == element:
            return mid
        elif array[mid] >= array[low]: # left half is sorted
            if element >= array[low] and element < array[mid]:
                return _helper(low, mid - 1)
            return _helper(mid + 1, high)
        if element < array[mid] and array[high] >= element:
            return _helper(low, mid - 1)
        return _helper(mid + 1, high)
        
    return _helper(0, len(array) - 1)


def main():
    array = [7,8,9,10,1,2,3,4,5]
    print(search_smallest_in_cyclically_sorted_array(array))
    print(search_element_in_cyclically_sorted_array(array, 5))


if __name__ == "__main__":
    main()

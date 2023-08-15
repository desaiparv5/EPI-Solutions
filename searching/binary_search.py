def binary_search(array, element):
    def binary_search_helper(low, high):
        if low > high:
            return -1
        mid = low + (high - low)//2
        if array[mid] == element:
            return mid
        elif element < array[mid]:
            return binary_search_helper(low, mid - 1)
        return binary_search_helper(mid + 1, high)

    return binary_search_helper(0, len(array) - 1)

def main():
    sorted_array = [2,3,4,5,6,7,8]
    element = 2
    print(binary_search(sorted_array, element))


if __name__ == "__main__":
    main()

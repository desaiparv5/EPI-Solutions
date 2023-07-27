"""Delete duplicate values from a sorted array"""


def delete_duplicates_from_sorted_array(arr):
    write_index = 1
    for ind in range(1, len(arr)):
        if arr[ind] != arr[ind - 1]:
            arr[write_index] = arr[ind]
            write_index += 1
    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1


def remove_occurances_of_element(arr, element):
    write_index = 0
    for ind in range(len(arr)):
        if arr[ind] != element:
            arr[write_index] = arr[ind]
            write_index += 1
    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1


def remove_elements_if_occurrs_m_times(arr, m):
    """Delete element if it occurs m times it appears occurs min(2, m) times"""
    if m == 1:
        delete_duplicates_from_sorted_array(arr)
        return
    write_index = 1
    count = 1
    for ind in range(1, len(arr)):
        if arr[ind] == arr[ind - 1]:
            count += 1
        else:
            count = 1
        if count == m:
            write_index -= (m - 2)
            count = 2

        arr[write_index] = arr[ind]
        write_index += 1
    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1


def main():
    test_arr = [1,2,2,3,4,5,5,5,5,6,6,6,7]

    arr = test_arr.copy()
    delete_duplicates_from_sorted_array(arr)
    print(arr)

    arr = test_arr.copy()
    remove_occurances_of_element(arr, 6)
    print(arr)

    arr = test_arr.copy()
    remove_elements_if_occurrs_m_times(arr, 3)
    print(arr)


if __name__ == "__main__":
    main()

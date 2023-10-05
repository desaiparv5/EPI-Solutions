def merge_sorted_arrays(array1, array2, len1, len2):
    write_pointer = len1 + len2 - 1
    pointer1 = len1 - 1
    pointer2 = len2 - 1
    while pointer1 >= 0 and pointer2 >= 0:
        if array1[pointer1] > array2[pointer2]:
            array1[write_pointer] = array1[pointer1]
            pointer1 -= 1
        else:
            array1[write_pointer] = array2[pointer2]
            pointer2 -= 1
        write_pointer -= 1
    while pointer1 >= 0:
        array1[write_pointer] = array1[pointer1]
        pointer1 -= 1
        write_pointer -= 1
    while pointer2 >= 0:
        array1[write_pointer] = array2[pointer2]
        pointer2 -= 1
        write_pointer -= 1


def main():
    array1 = [3,5,8,8,10,None,None,None,None,None,None,None]
    array2 = [1,2,11]
    merge_sorted_arrays(array1, array2, 5, 3)
    print(array1)


if __name__ == "__main__":
    main()

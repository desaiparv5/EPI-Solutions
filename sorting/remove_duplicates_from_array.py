def remove_duplicates(array):
    array.sort()
    write_index = 0
    read_index = 1
    while read_index < len(array):
        if array[write_index] == array[read_index]:
            read_index += 1
        else:
            array[write_index+1] = array[read_index]
            write_index += 1
            read_index += 1
    del array[write_index+1:]


def main():
    array = [1,2,3,3,4,4,4,4,6,6,6,6]
    remove_duplicates(array)
    print(array)


if __name__ == "__main__":
    main()

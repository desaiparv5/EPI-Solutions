def replace_and_remove_a_b(s):
    write_index = 0
    a_count = 0
    curr_index = 0
    while curr_index < len(s):
        if s[curr_index] != 'b':
            s[write_index] = s[curr_index]
            write_index += 1
        if s[curr_index] == 'a':
            a_count += 1
        curr_index += 1

    curr_index = write_index - 1
    write_index += (a_count - 1)
    while curr_index >= 0:
        if s[curr_index] == 'a':
            s[write_index] = 'd'
            s[write_index - 1] = 'd'
            write_index -= 1
        else:
            s[write_index] = s[curr_index]
        write_index -= 1
        curr_index -= 1


def telex_encoding(s):
    curr_index = 0
    extra_space = 0
    write_index = 0

    encoding = {
        ",": ["c", "o", "m", "m", "a"],
        "?": ["Q","U","E","S","T","I","O","N"," ","M","A","R","K"],
        "!": ["E","X","C","L","A","M","A","T","I","O","N"," ","M","A","R","K"],
        ".": ["D", "O", "T"],
    }
    while curr_index < len(s) and s[curr_index] != "":
        if s[curr_index] in encoding:
            extra_space += len(encoding[s[curr_index]]) - 1
        curr_index += 1

    curr_index -= 1
    write_index = curr_index + extra_space

    while curr_index >= 0:
        if s[curr_index] in encoding:
            replacement = encoding[s[curr_index]]
            for char in replacement[::-1]:
                s[write_index] = char
                write_index -= 1
        else:
            s[write_index] = s[curr_index]
            write_index -= 1
        curr_index -= 1


def merge_two_sorted_arrays(arr1, arr2):
    arr1_index = 0
    while arr1[arr1_index]:
        arr1_index += 1
    arr1_index -= 1
    arr2_index = len(arr2) - 1
    write_index = arr1_index + arr2_index + 1
    while arr2_index >= 0:
        if arr1[arr1_index] > arr2[arr2_index]:
            arr1[write_index] = arr1[arr1_index]
            arr1_index -= 1
        else:
            arr1[write_index] = arr2[arr2_index]
            arr2_index -= 1
        write_index -= 1


def main():
    s = ['b', 'b', 'b', 'b']
    replace_and_remove_a_b(s)
    print(s)

    s = ["s",".","w","a","t","?","","","","","","","","","","","","","",""]
    telex_encoding(s)
    print(s)

    arr1 = [1,2,3,7,"","",""]
    arr2 = [4,5,6]
    merge_two_sorted_arrays(arr1, arr2)
    print(arr1)


if __name__ == "__main__":
    main()

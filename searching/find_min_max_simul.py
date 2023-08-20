def find_min_max(array):
    if len(array) % 2:
        min_val, max_val = array[0], array[0]
        curr_index = 1
    else:
        if array[0] >= array[1]:
            min_val, max_val = array[1], array[0]
        else:
            min_val, max_val = array[0], array[1]
        curr_index = 2
    while curr_index < len(array) - 1:
        if array[curr_index] > array[curr_index + 1]:
            max_val = max(max_val, array[curr_index])
            min_val = min(min_val, array[curr_index + 1])
        else:
            max_val = max(max_val, array[curr_index + 1])
            min_val = min(min_val, array[curr_index])
        curr_index += 2
    return min_val, max_val

def main():
    array = [9,0,10,1,10,9,8,-1]
    print(find_min_max(array))


if __name__ == "__main__":
    main()

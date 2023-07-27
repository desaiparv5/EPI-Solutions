"""Sort array of even and odd integers. So that even numbers come first and odd later"""
def sort_even_odd_array(arr):
    # constant space
    even_index = 0
    odd_index = len(arr) - 1

    while even_index < odd_index:
        if arr[even_index] & 1:
            arr[even_index], arr[odd_index] = arr[odd_index], arr[even_index]
            odd_index -= 1
        else:
            even_index += 1


def main():
    arr = [2,7,3,0,1,5,2,3,1,10]
    sort_even_odd_array(arr)
    print(arr)


if __name__ == "__main__":
    main()

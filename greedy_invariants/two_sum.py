def has_two_sum(arr, target):
    arr.sort()
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return True
        elif  arr[i] + arr[j] > target:
            j -= 1
        else:
            i+=1
    return False


def main():
    print(has_two_sum([1,3,8,0,-9,2,7], 5))


if __name__ == "__main__":
    main()

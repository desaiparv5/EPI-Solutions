def find_missing_duplicate_element(array):
    xr = 0
    for ind, val in enumerate(array):
        xr ^= ind ^ val
    
    last_set_bit, miss_or_dup = xr & ~(xr - 1), 0

    for ind, val in enumerate(array):
        if last_set_bit & val:
            miss_or_dup ^= val
        if last_set_bit & ind:
            miss_or_dup ^= ind

    if miss_or_dup in array:
        return miss_or_dup, miss_or_dup ^ xr
    return miss_or_dup ^ xr, miss_or_dup


def main():
    array = [0,1,2,3,7,5,6,7,8]
    print(find_missing_duplicate_element(array))


if __name__ == "__main__":
    main()

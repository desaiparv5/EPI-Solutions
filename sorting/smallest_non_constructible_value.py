def smallest_non_constructible_value(array):
    max_constructible_value = 0
    array.sort()
    for i in array:
        if i > max_constructible_value + 1:
            break
        max_constructible_value += i
    return max_constructible_value + 1


def main():
    array = [12,2,1,15,2,4]
    print(smallest_non_constructible_value(array))


if __name__ == "__main__":
    main()

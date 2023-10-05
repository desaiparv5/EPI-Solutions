def intersection_of_sorted_arrays(array1, array2):
    ind1 = 0
    ind2 = 0
    intersection = []
    while ind1 < len(array1) and ind2 < len(array2):
        if array1[ind1] == array2[ind2]:
            if ind1 == 0 or array1[ind1] != array1[ind1-1]:
                intersection.append(array1[ind1])
        if array2[ind2] <= array1[ind1]:
            ind2 += 1
        else:
            ind1 += 1
    return intersection


def main():
    array1 = [2,3,3,5,6,10]
    array2 = [1,3,7,10]
    print(intersection_of_sorted_arrays(array1, array2))


if __name__ == "__main__":
    main()

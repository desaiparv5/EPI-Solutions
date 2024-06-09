from primitive_types.generate_random_numbers import generate_random_number


def generate_random_permutation(arr):
    index_vector = [_ for _ in range(len(arr))]

    for ind in range(len(arr)):
        random_vector_index = generate_random_number(ind, len(arr) - 1)
        random_index = index_vector[random_vector_index]
        arr[random_index], arr[ind] = arr[ind], arr[random_index]
        index_vector[ind], index_vector[random_index] = index_vector[random_index], index_vector[ind]


def main():
    arr = [1,2,3,4,5,6,7]
    generate_random_permutation(arr)
    print(arr)


if __name__ == "__main__":
    main()

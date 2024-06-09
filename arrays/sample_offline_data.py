from primitive_types.generate_random_numbers import generate_random_number

def sample_data(arr, k):
    curr_ind = 0
    sample_data = []
    while curr_ind < k:
        rand_ind = generate_random_number(curr_ind, len(arr) - 1)
        sample_data.append(arr[rand_ind])
        arr[rand_ind], arr[curr_ind] = arr[curr_ind], arr[rand_ind]
        curr_ind += 1
    return sample_data


def main():
    arr = [2, 6 ,5 ,9, 3, 7, 4, 0]
    k = 4
    print(sample_data(arr, k))


if __name__ == "__main__":
    main()

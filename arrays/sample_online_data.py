from primitive_types.generate_uniform_random_numbers import generate_random_number

def data_gen():
    for i in range(10_000):
        yield i


def sample_online_data(input_stream, k):
    random_data = [next(input_stream) for _ in range(k)]
    
    num_seen = k
    for num in input_stream:
        num_seen += 1
        random_index = generate_random_number(0, num_seen)
        if random_index <= k - 1:
            random_data[random_index] = num
    return random_data


def main():
    input_stream = data_gen()
    k = 25
    print(sample_online_data(input_stream, k))


if __name__ == "__main__":
    main()

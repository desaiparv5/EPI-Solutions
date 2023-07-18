"""Multiply 2 numbers only using binary or logical operations"""


import random
import time


def add(a, b):
    temp_a = a
    temp_b = b
    while temp_b:
        data = temp_a & temp_b
        temp_a ^= temp_b
        temp_b = data << 1

    return temp_a


def multiply(a, b):
    res = 0
    while a:
        if a & 1:
            res |= add(res, b)
        a >>= 1
        b <<= 1
    return res


def main():
    num_bits = 6400
    # int_a = random.randint(2**num_bits, 2**(num_bits + 1))
    int_a = 8
    # int_b = random.randint(2**num_bits, 2**(num_bits + 1))
    int_b = 4

    print(f"Multiplying numbers {int_a} and {int_b}")
    print("Using bitwise multiplication")
    start_time = time.process_time_ns()
    print(multiply(int_a, int_b))
    print(f"Time taken: {time.process_time_ns() - start_time}")


    print("Using inbuilt operator")
    start_time = time.process_time_ns()
    print(int_a * int_b)
    print(f"Time taken: {time.process_time_ns() - start_time}")


if __name__ == "__main__":
    main()

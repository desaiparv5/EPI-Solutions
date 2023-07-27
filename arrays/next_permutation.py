"""Multiply arbitrary precision integers."""
from time import process_time_ns
import random


def multiply_precision_integers(int_arr1, int_arr2):
    res_arr = [0 for _ in range(len(int_arr1) + len(int_arr2))]
    for i in range(len(int_arr1) - 1, -1, -1):
        carry = 0
        for j in range(len(int_arr2) - 1, -1, -1):
            s = int_arr1[i] * int_arr2[j] + carry + res_arr[i+j+1]
            res_arr[i+j+1] = s % 10
            carry = s // 10
        res_arr[i + j] += carry
    res_arr[0] = carry
    return res_arr


def main():
    int_arr1 = [random.randint(0, 9) for _ in range(10)]
    int_arr2 = [random.randint(0, 9) for _ in range(10)]
    print(int_arr1)
    print(int_arr2)
    start_time = process_time_ns()
    res_arr = multiply_precision_integers(int_arr1, int_arr2)
    print(f"Time taken: {process_time_ns() - start_time}")
    print(res_arr)


if __name__ == "__main__":
    main()

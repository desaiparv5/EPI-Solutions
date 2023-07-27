"""Increment an arbitrary precision integer"""
import random
from time import process_time_ns


def increment_arbitrary_integer(int_arr):
    int_arr[-1] += 1
    carry = int_arr[-1] // 10
    int_arr[-1] %= 10

    end = len(int_arr) - 2
    while carry and end >= 0:
        int_arr[end] += carry
        carry = int_arr[end] // 10
        int_arr[end] %= 10

        end -= 1

    if carry: return [carry] + int_arr
    else: return int_arr


def add_arbitrary_binary(bit_arr1, bit_arr2):
    ind1 = len(bit_arr1) - 1
    ind2 = len(bit_arr2) - 1
    sum = []
    carry = 0
    while ind1 >= 0 and ind2 >= 0:
        sum.append((bit_arr1[ind1] ^ bit_arr2[ind2]) ^ carry)
        carry = (bit_arr1[ind1] & bit_arr2[ind2]) | (carry & (bit_arr1[ind1] ^ bit_arr2[ind2]))
        ind1 -= 1
        ind2 -= 1

    while ind1 >= 0:
        sum.append(bit_arr1[ind1] ^ carry)
        carry = (carry & bit_arr1[ind1])
        ind1 -= 1
    
    while ind2 >= 0:
        sum.append(bit_arr2[ind2] ^ carry)
        carry = (carry & bit_arr2[ind2])
        ind1 -= 1
    
    if carry: sum.append(carry)
    return sum[::-1]

def main():
    int_arr = [random.randint(0, 9) for _ in range(10)]
    print(int_arr)
    start_time = process_time_ns()
    int_arr = increment_arbitrary_integer(int_arr)
    print(f"Time taken: {process_time_ns() - start_time}")
    print(int_arr)

    bit_arr1 = [random.randint(0, 1) for _ in range(10)]
    bit_arr2 = [random.randint(0, 1) for _ in range(5)]
    print(bit_arr1)
    print(bit_arr2)
    start_time = process_time_ns()
    res_arr = add_arbitrary_binary(bit_arr1, bit_arr2)
    print(f"Time taken: {process_time_ns() - start_time}")
    print(res_arr)

if __name__ == "__main__":
    main()

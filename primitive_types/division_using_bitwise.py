"""Divide 2 numbers only using binary or logical operations"""
# NOT WORKING

import time
from multiplication_using_bitwise import add


NUM_BITS = 8

def subtract(a, b):
    b = add(~b, 1)
    c = add(a, b)
    return c


def get_absolute_value_bitwise(num):
    mask = num << (NUM_BITS - 1)
    return subtract(mask^num, mask)


def get_sign_bitwise(num):
    return (num >> (NUM_BITS - 1)) & 1


def division(x, y):
    if not y:
        raise Exception("Zero division error")
    ans = 0
    abs_x = get_absolute_value_bitwise(x)
    abs_y = get_absolute_value_bitwise(y)
    sign = get_sign_bitwise(x) ^ get_sign_bitwise(y)
    while abs_x >= abs_y:
        quotient = 0
        while abs_x > (y << quotient):
            quotient += 1
        ans += (1 << quotient)
        abs_x = subtract(abs_x, abs_y << quotient)
    return ans

# int_a = random.randint(2**num_bits, 2**(num_bits + 1))
int_a = 28
# int_b = random.randint(2**num_bits, 2**(num_bits + 1))
int_b = 4


def bitwise_division(dividend, divisor):
    # edge case when divisor is 0
    if not divisor:
        return None

    quotient = 0
    power = NUM_BITS  # maximum power of 2 for 32-bit integers

    # reduce the divisor to the nearest power of 2
    while divisor << power > dividend:
        power = subtract(power, 1)

    # perform the division using bit shifting and subtraction
    while power >= 0:
        if dividend >= divisor << power:
            dividend -= divisor << power
            quotient |= 1 << power
        power = subtract(power, 1)

    return quotient

print(f"Divding {int_a} / {int_b}")
print("Using bitwise division")
start_time = time.process_time_ns()
print(bitwise_division(int_a, int_b))
print(f"Time taken: {time.process_time_ns() - start_time}")
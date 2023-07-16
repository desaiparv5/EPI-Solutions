"""Find closest integer with same weight"""
import random
import time


num_bits = 100000*8


def closest_integer_same_weight(word):
    # Find closest integer with same weight. Weight is number of weights set in a word
    for i in range(num_bits):
        if ((word >> i) & 1) != ((word >> (i + 1)) & 1):
            word ^= (1 << i) | (1 << (i + 1))
            return word
    raise Exception("All bits are 1s or 0s")

def closest_integer_same_weight_faster(word):
    # Find closest integer with same weight. Weight is number of weights set in a word
    least_significant_bit_set = word & ~(word - 1)

    if least_significant_bit_set == word:
        raise Exception("All bits are 0s")

    least_significant_bit_not_set = ~word & (word + 1)

    if least_significant_bit_not_set > least_significant_bit_set:
        word |= least_significant_bit_not_set
        word ^= least_significant_bit_not_set >> 1
    else:
        word ^= least_significant_bit_set
        word |= least_significant_bit_set >> 1
    return word


word = random.randint(2**num_bits, 2**(num_bits + 1))
print(f"Closest integer with same weight of: {word}")

print("Using standard method")
start_time = time.process_time_ns()
closest_integer_same_weight(word=word)
print(f"Time taken: {time.process_time_ns() - start_time} nanoseconds")

print("Using faster method")
start_time = time.process_time_ns()
closest_integer_same_weight_faster(word=word)
print(f"Time taken: {time.process_time_ns() - start_time} nanoseconds")

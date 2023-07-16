"""Calculating parity of a word"""
import time
import random


# bit-hacking methods here: https://graphics.stanford.edu/~seander/bithacks.html

def naive_method(word):
    # Naive way
    # this method goes over every bit
    result = 0
    while word:
        result ^= word & 1
        word >>= 1
    return result


def faster_method(word):
    # Brian Kernighan's method
    # this method sets the number to the number till its next set bit
    result = 0
    while word:
        result ^= 1
        word &= word - 1
    return result


def parity_of_large_data(word):
    # Calculate parity of a large word.
    # Uses caching and masking technique. We store a look up table of precomputed parties
    # This method calculates parity of a large word by dividing word into 4 parts
    # This method gets faster as we increase the word size and lookup table size

    parity_lookup_table = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 
                           1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 
                           1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 
                           0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 
                           1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 
                           0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 
                           0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 
                           0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 
                           1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 
                           0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 
                           0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 
                           0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 
                           0, 1, 1, 0]  # precomputed parities of 8 bit words
    k_bit_mask = 0xFF
    word_size = 8
    result = 0
    while word:
        result ^= parity_lookup_table[word & k_bit_mask]
        word >>= word_size
    return result


num_bits = 90000

word = random.randint(2**num_bits, 2**(num_bits + 1))
print(f"Calculating parity of: {word}")

print("Using naive method")
start_time = time.process_time_ns()
print(naive_method(word=word))
print(f"Time taken: {time.process_time_ns() - start_time} nanoseconds")


print("Using faster method")
start_time = time.process_time_ns()
print(faster_method(word=word))
print(f"Time taken: {time.process_time_ns() - start_time} nanoseconds")

print("Using masking method for large numbers")
start_time = time.process_time_ns()
print(parity_of_large_data(word=word))
print(f"Time taken: {time.process_time_ns() - start_time} nanoseconds ")

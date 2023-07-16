# Reversing the bits of a word


import random
import time


def reverse_bits(word):
    # Reverses bits of 16 bit word
    precomputed_reverse = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    word_size = 4
    k_bit_mask = 0xF
    return (
        precomputed_reverse[word & k_bit_mask] << (3 * word_size)
        | precomputed_reverse[(word >> word_size) & k_bit_mask] << (2 * word_size)
        | precomputed_reverse[(word >> (2 * word_size)) & k_bit_mask] << word_size
        | precomputed_reverse[(word >> (3 * word_size)) & k_bit_mask]
    )


word = random.randint(2**15, 2**16)

print(f"Reversing bits of word: {word}")
start_time = time.process_time_ns()
print(reverse_bits(word))
print(f"Time taken: {time.process_time_ns() - start_time}")

# Swap bits of a number
import time
import random


def swap_bits(word, i, j):
    if ((word >> i) & 1) != ((word >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        word ^= bit_mask
    return word

word = random.randint(2**9, 2**10)
pos_a = random.randint(0, 9)
pos_b = random.randint(0, 9)

print(f"Swapping bits {pos_a} and {pos_b} of word: {word}")
start_time = time.process_time_ns()
print(swap_bits(word, pos_a, pos_b))
print(f"Time taken: {time.process_time_ns() - start_time}")

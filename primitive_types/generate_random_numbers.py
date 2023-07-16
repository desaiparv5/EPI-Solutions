"""Generate random numbers with uniformity"""
import random


def zero_one_random():
    return random.randrange(2)


def generate_random_number(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


def main():
    print(generate_random_number(1, 6))


if __name__ == "__main__":
    main()

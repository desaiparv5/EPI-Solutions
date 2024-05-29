def gray_code(n):
    def helper(num_bits):
        if num_bits == 1:
            return [0, 1]
        gray_codes_num_bits_minus_1 = helper(num_bits - 1)
        return gray_codes_num_bits_minus_1 + [1<<(num_bits-1) | i for i in reversed(gray_codes_num_bits_minus_1)]
    return helper(n)



def main():
    print(gray_code(3))


if __name__ == "__main__":
    main()

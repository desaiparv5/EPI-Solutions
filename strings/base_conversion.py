def base_to_decimal(num_list, base):
    decimal_num = 0
    current_place = 1
    for num in num_list[::-1]:
        decimal_num += current_place * num
        current_place *= base
    
    return decimal_num


def decimal_to_base(num, base):
    out_list = []
    while num:
        out_list.append(num % base)
        num //= base
    return out_list[::-1]


def convert_base(num_list, base1, base2):
    num = base_to_decimal(num_list, base1)
    out_num_list = decimal_to_base(num, base2)
    return out_num_list


def main():
    num_list = [1, 0, 1, 1]
    base1 = 2
    base2 = 8
    print(convert_base(num_list, base1, base2))


if __name__ == "__main__":
    main()

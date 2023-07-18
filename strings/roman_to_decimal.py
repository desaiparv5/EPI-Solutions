DECIMAL_TO_ROMAN_MAPPING = [
    (1, "I"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M")
]

ROMAN_TO_DECIMAL_MAPPING = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_decimal(roman_number):
    num = ROMAN_TO_DECIMAL_MAPPING[roman_number[-1]]
    curr_index = len(roman_number) - 2
    while curr_index >= 0:
        curr_letter = ROMAN_TO_DECIMAL_MAPPING[roman_number[curr_index]]
        next_letter = ROMAN_TO_DECIMAL_MAPPING[roman_number[curr_index + 1]]
        if curr_letter < next_letter:
            num -= curr_letter
        else:
            num += curr_letter
        curr_index -= 1
    return num


def decimal_to_roman(decimal_number):
    curr_roman_index = len(DECIMAL_TO_ROMAN_MAPPING) - 1
    roman_number = ""
    while decimal_number:
        curr_num, curr_roman = DECIMAL_TO_ROMAN_MAPPING[curr_roman_index]
        if decimal_number >= curr_num:
            roman_number += curr_roman
            decimal_number -= curr_num
        else:
            curr_roman_index -= 1
    return roman_number


def is_valid_roman_number(roman_number):
    decimal_num = roman_to_decimal(roman_number)
    return roman_number == decimal_to_roman(decimal_num)


def main():
    roman_number = "MCMXCIIV"
    decimal_number = 1995
    print(roman_to_decimal(roman_number))
    print(decimal_to_roman(decimal_number))
    print(is_valid_roman_number(roman_number))


if __name__ == "__main__":
    main()

def string_to_integer(string: str):
    is_neg = False
    if string.startswith('-'):
        is_neg = True
        string = string[1:]
    num = 0
    for char in string:
        num *= 10
        num += int(char)
    return -num if is_neg else num

    
def integer_to_string(num):
    int_list = []

    is_neg = num < 0
    num = abs(num)
    while num:
        int_list.append(str(num % 10))
        num //= 10

    return ('-' if is_neg else '') + ''.join(int_list[::-1])

def main():
    print(string_to_integer("-1234"))
    print(integer_to_string(-1234))


if __name__ == "__main__":
    main()

def sinusodial_string(s):
    sinusodial_list = [''] * len(s)
    curr_index = 0
    for i in range(1, len(s), 4):
        sinusodial_list[curr_index] = s[i]
        curr_index += 1
    for i in range(0, len(s), 2):
        sinusodial_list[curr_index] = s[i]
        curr_index += 1
    for i in range(3, len(s), 4):
        sinusodial_list[curr_index] = s[i]
        curr_index += 1
    return sinusodial_list


def main():
    print(sinusodial_string("Hello world"))


if __name__ == "__main__":
    main()

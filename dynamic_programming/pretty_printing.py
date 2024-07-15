def pretty_print(words, line_length):
    # TODO: Didn't understand the solution. This is pretty tough.
    num_remaining_blanks = line_length - words[0]
    messiness = [num_remaining_blanks**2] + [float("inf")]*(len(words) - 1)
    for i in range(1, len(words)):
        num_remaining_blanks = line_length - words[i]
        messiness[i] = messiness[i-1] + num_remaining_blanks ** 2
        for j in reversed(range(i)):
            num_remaining_blanks -= words[j] + 1
            if num_remaining_blanks < 0:
                break
            first_j_messiness = 0 if j - 1 < 0 else messiness[j-1]
            curr_messiness = num_remaining_blanks ** 2
            messiness[i] = min(messiness[j-1], curr_messiness+first_j_messiness)
    return messiness[-1]


def pretty_print(words, line_length):
    # TODO: Solve the same problem when the messiness is the sum of the messinesses of all but the
    # last line.
    pass


def pretty_print(words, line_length):
    # TODO: Suppose the messiness of a line ending with b blank characters is defined to be b. Can you
    # solve the messiness minimization problem nO(n) time and O(1) space?
    pass


def main():
    words = [5,4,9]
    line_length = 10
    print(pretty_print(words, line_length))


if __name__ == "__main__":
    main()

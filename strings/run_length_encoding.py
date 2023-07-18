def run_length_encoding(s):
    if not s: return None
    curr_index = 1
    encoded_string = ""
    curr_count = 1
    curr_char = s[0]
    while curr_index < len(s):
        if curr_char == s[curr_index]:
            curr_count += 1
        else:
            encoded_string += f"{curr_char}{curr_count}"
            curr_count = 1
            curr_char = s[curr_index]
        curr_index += 1

    return encoded_string + f"{curr_char}{curr_count}"


def run_length_decoding(s):
    if len(s) % 2: raise Exception
    decoded_string = ""
    curr_index = 0
    while curr_index < len(s):
        char = s[curr_index]
        count = int(s[curr_index + 1])
        curr_index += 2
        decoded_string += char * count
    return decoded_string



def main():
    s = "aaabccccce"
    encoded_string = run_length_encoding(s)
    assert s == run_length_decoding(encoded_string)


if __name__ == "__main__":
    main()

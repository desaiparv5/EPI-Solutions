def look_and_say(n):
    def look_and_say_helper(prev, index):
        if index == len(prev):
            return ""
        curr_index = index
        count = 1
        while curr_index < (len(prev) - 1) and prev[curr_index] == prev[curr_index + 1]:
            count += 1
            curr_index += 1
        
        return f"{count}{prev[index]}" + look_and_say_helper(prev, curr_index + 1)

    curr_num = "1"
    for _ in range(1, n):
        curr_num = look_and_say_helper(curr_num, 0)
    return curr_num


def main():
    for i in range(10):
        print(look_and_say(i))


if __name__ == "__main__":
    main()

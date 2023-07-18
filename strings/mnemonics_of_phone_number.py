mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def mneumonics_of_phone_number(phone_number):
    def mneumonic_helper(pre_str_list, curr_index):
        if curr_index >= len(phone_number):
            return pre_str_list
        
        arr = []
        for char in mapping[int(phone_number[curr_index])]:
            for pre_str in pre_str_list:
                arr.append(pre_str + char)
        return mneumonic_helper(arr, curr_index + 1)
    
    return mneumonic_helper([''], 0)


def mneumonic_phone_number_back_tracking(phone_number):
    result = []
    combination = ["" for _ in range(len(phone_number))]

    def mneumonic_helper(combination, curr_index):
        if curr_index == len(phone_number):
            return result.append("".join(combination))
        for letter in mapping[int(phone_number[curr_index])]:
            combination[curr_index] = letter
            mneumonic_helper(combination, curr_index+1)

    mneumonic_helper(combination, 0)
    return result


def mneumonic_phone_number_no_recursion(phone_number):
    result = []
    queue = []

    queue.append("")
    while len(queue):
        s = queue.pop()
        if len(s) == len(phone_number):
            result.append(s)
        else:
            for letter in mapping[int(phone_number[len(s)])]:
                queue.append(s + letter)
    return result


def main():
    phone_number = "23"
    print(mneumonics_of_phone_number(phone_number))
    print(mneumonic_phone_number_back_tracking(phone_number))
    print(mneumonic_phone_number_no_recursion(phone_number))


if __name__ == "__main__":
    main()

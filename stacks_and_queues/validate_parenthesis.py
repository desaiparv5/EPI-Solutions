from stack_and_queue import Stack


def validate_parenthesis(string: str):
    stack = Stack()
    for char in string:
        if char in ("(", "[", "{"):
            stack.push(char)
        else:
            open_bracket = stack.pop()
            if not open_bracket:
                raise Exception
            if (char == ")" and open_bracket!= "(") or (char == "]" and open_bracket != "[") or (char == "}" and open_bracket != "{"):
                    raise Exception
    if stack.peek():
        raise Exception

def main():
    string = "{[{()()()}]}"
    print(validate_parenthesis(string))


if __name__ == "__main__":
    main()

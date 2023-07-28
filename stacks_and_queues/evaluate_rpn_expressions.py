from stack_and_queue import Stack


def evaluate_rpn_expression(rpn_expression: str):
    stack = Stack()
    for val in rpn_expression.split(","):
        if val in ("+", "-", "*", "/"):
            opr2 = stack.pop()
            opr1 = stack.pop()
            if val == "+":
                res = opr1 + opr2
            elif val == "-":
                res = opr1 - opr2
            elif val == "/":
                res = int(opr1 / opr2)
            else:
                res = opr1 * opr2
            stack.push(res)
        else:
            stack.push(int(val))
    return stack.pop()


def main():
    rpn_expression = "10,6,9,3,+,-11,*,/,*,17,+,5,+"
    print(evaluate_rpn_expression(rpn_expression))


if __name__ == "__main__":
    main()

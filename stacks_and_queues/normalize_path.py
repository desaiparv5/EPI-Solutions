from stack_and_queue import Stack


def normalize_path(path: str):
    stack = Stack()
    for dir in path.split("/"):
        if dir == "..":
            stack.pop()
        elif dir == "." or dir == "":
            continue
        else:
            stack.push(dir)
    final_path_list = []
    while stack:
        final_path_list.append(stack.pop())
    final_path_list.reverse()

    if path.startswith("/"):
        final_path = "/"
    else:
        final_path = ""
    final_path += "/".join(final_path_list)
    return final_path


def main():
    path = "/bin//gcc/../scripts/./hello.txt"
    print(normalize_path(path))


if __name__ == "__main__":
    main()

def majority_element(arr):
    votes, candidate = 0, None
    for elem in arr:
        if votes == 0:
            candidate = elem
            votes += 1
        elif elem == candidate:
            votes += 1
        else:
            votes -= 1
    return candidate


def main():
    print(majority_element(['b','a','c','a','a','b','a','a','c','a']))


if __name__ == "__main__":
    main()

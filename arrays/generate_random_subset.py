import random


def random_subset(n, k):
    H = {}
    for i in range(k):
        r = random.randrange(i, n)
        rmap = H.get(r, r)
        imap = H.get(i, i)
        H[r] = imap
        H[i] = rmap
    return [H[i] for i in range(k)]

def main():
    n = 10_000
    k = 25
    print(random_subset(n, k))


if __name__ == "__main__":
    main()

"""Generate primes till n"""

def generate_primes(n):
    """Sieve of Eratosthenes"""
    primes = [True for _ in range(n)]

    i = 2
    while i*i <= n:
        if primes[i]:
            for j in range(i*2, n, i):
                primes[j] = False
        i += 1

    for i in range(2, len(primes)):
        if primes[i]:
            print(i, end=" ")


def main():
    n = 100
    generate_primes(n)


if __name__ == "__main__":
    main()

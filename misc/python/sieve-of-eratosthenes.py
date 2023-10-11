# SIEVE OF ERATOSTHENES

def sieve_of_eratosthenes(n: int) -> list:
    """Generate primes up to `n` using the sieve of Eratosthenes."""
    primes: list = []
    sieve: list = [True] * (n + 1)

    # loop through list
    for p in range(2, n + 1):
        if sieve[p]:
            # next True is prime
            primes.append(p)

            for i in range(p, n + 1, p):
                # mark all multiples of primes as False
                sieve[i] = False

    return primes


print(sieve_of_eratosthenes(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
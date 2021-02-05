def solve(n):
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(j * j, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

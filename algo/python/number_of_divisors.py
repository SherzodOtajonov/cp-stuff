# algo to find the number of divisors of a number n in O(sqrt(n)) time
def d_n(n):
    from math import sqrt
    count = 0
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            if i == n/i:
                count += 1
            else:
                count += 2
    return count

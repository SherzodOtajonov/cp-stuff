n = int(input())
A = [int(i) for i in input().split()]
def func(A, n):
    A.sort()
    res = 0
    for i in range(n):
        res += A[i] * (2 * i - n + 1)
    return res
print(func(A, n))

t = int(input())

while 0:
    #input()
    #a = list(map(int, input().split()))
    if not sum(a): print('NO')
    else:
        a.sort()
        s=0
        for i in range(len(a)):
            j=i+1
            while not s+a[i]:
                a[i], a[j] = a[j],a[i]
                j+=1
        print(a)   


from math import sqrt
def solve(n): #n>1
    A = [1 for i in range(2, n)]
    for i in range(2, int(sqrt(n))+1):
        if A[i]:
            for j in range(i**2, n):
                A[j] = 0
    r=[]
    for i in range(len(A)):
        if A[i]: r.append(i)
    return r
print(solve(t))

t = int(input())

def solve(a):
    l=[0,0,0]
    for i in range(len(a)):
        l[a[i]%3]+=1
    return l[0]+min(l[1:])+abs(l[1]-l[2])//3

for i in range(t):
    input()
    a = list(map(int, input().split()))
    print(solve(a))

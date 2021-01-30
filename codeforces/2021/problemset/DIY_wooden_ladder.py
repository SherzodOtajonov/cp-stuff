t = int(input())
 
def solve(a):
    a.sort()
    if len(a)<=2: return 0
    if len(a) == 3 and 1 < a[1]: return 1
    if len(a) == 3 and 1 == a[1]: return 0
 
    b = a[-2]
    s= min(b-1, len(a)-2)
    return s
       
 
for i in range(t):
    input()
    a = list(map(int, input().split()))
    print(solve(a))

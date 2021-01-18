t = int(input())
 
def solve(x):
    if x > 45: return '-1'
    res = ''
    res_sum = 0
    org = x
    for i in range(9, 0, -1):
        if i <= x:
            res += str(i)
            res_sum += i
            x -= i
            if res_sum == org:
                return res[::-1]
            elif res_sum > org:
                return '-1'
for i in range(t):
    x = int(input())
    print(solve(x))

H, W = map(int, input().split(' '))

def solve(H, W):
    l = [list(map(int, input().split())) for i in range(H)]

    mn, sm = float('inf'), 0
    for j in l:
        mn = min(min(j), mn)
        sm += sum(j)

    return sm - (H*W*mn)

print(solve(H, W))

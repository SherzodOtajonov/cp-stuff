s = input()

w = 'hello'
def solve(s, w, i):
    if w[i] == 'o' and w[i] in s:
        return 'YES'
    elif w[i] == 'o' and w[i] not in s:
        return 'NO'
    try:
        c = s.index(w[i])
    except ValueError:
        return 'NO'
    return solve(s[c+1:], w, i+1)

print(solve(s, w, 0))

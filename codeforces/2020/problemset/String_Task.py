vowels = ["A", "O", "Y", "E", "U", "I"]

inp = input()

def solve(s):
    res = []
    for i in s:
        if i.upper() not in vowels:
            res.append('.'+i.lower())

    return ''.join(res)

print(solve(inp))

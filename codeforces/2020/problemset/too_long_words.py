n = int(input())


def solve(n, word):
    l = len(word)
    if l > 10:
        word = word[0] + str(l-2) + word[-1]
    return word

for i in range(n):
    word = input()
    print(solve(n, word))

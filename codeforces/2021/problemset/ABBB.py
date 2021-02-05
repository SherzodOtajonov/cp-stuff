= int(input())

for i in range(t):
    a = 0
    s = input()
    for j in range(len(s)):
        if s[i] == 'A':
            a+=1
        elif s[i] == 'B' and a: a-=1
    print(a)

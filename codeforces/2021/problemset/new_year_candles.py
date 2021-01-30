a, b = map(int, input().split())

r=a
while a>=b:
    r+= a//b
    a = a//b+a%b
print(int(r))

n=int(input())
h1=input()
h2=''
for i in range(n-1):
    if i==0: h2=input()[:3]
    else: input()
l=input()[-3:].strip()
print("home") if (l==h1 or l==h2) else print("contest")

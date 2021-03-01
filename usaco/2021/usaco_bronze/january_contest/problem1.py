# problem link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1083
s = input()
a = input()
r,j=1,0
for i in range(len(a)):
    if j==len(s):
        j=0
        r+=1
    while a[i]!=s[j]:
        j+=1
        if j==len(s):
            j=0
            r+=1
    j+=1
print(r, end='\n')

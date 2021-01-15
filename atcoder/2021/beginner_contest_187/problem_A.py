a, b = input().split(' ')
sa = sb = 0
for i in a:
    sa += int(i)
 
for j in b:
    sb += int(j)
 
print(max(sa, sb))

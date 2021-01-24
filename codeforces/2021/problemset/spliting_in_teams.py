from collections import Counter
input()
a = list(map(int, input().split(' ')))
c = Counter(a)
ones, twoes = c[1], c[2]
 
 
if not ones:
    print(0)
elif ones <= twoes:
    print(ones)
else:
    print(twoes+(ones-twoes)//3)

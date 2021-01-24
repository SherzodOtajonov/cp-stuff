i = int(input())
 
if i % 10 == 0: print(i)
elif i%10>5: print(i+(10-i%10))
else: print(i-(i%10))

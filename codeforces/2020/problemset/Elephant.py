x = int(input())

def solve(x):
	from math import ceil
	if x<6: return 1
	else: return ceil(x/5)

print(solve(x))

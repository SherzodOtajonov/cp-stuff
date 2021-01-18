a, b = [int(i) for i in input().split()]

c = 0
def solve(a, b):
	global c
	if a > b:
		return c
	c+=1
	return solve(a*3, b*2)

print(solve(a, b))

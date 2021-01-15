nm, k = [int(i) for i in input().split()]

def solve(nm):
	global k
	if k <=0: return nm
	if not nm%10:
		k-=1
		return solve(nm/10)
	k-=1
	return solve(nm-1)

print(solve(nm))

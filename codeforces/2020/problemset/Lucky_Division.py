n = int(input())

def solve(n):
	lucky1 = [4, 7]
	lucky2 = set('47')
	if set(str(n)) == lucky2 or n in lucky1: return 'YES'
	for i in range(n):
		if (i in lucky1 or set(str(i)) == lucky2) and n%i == 0:
			return 'YES'
	return 'NO'

print(solve(n))

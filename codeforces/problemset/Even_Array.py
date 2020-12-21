t = int(input())

def solve(a):
	evens = odds = 0
	for i in range(len(a)):
		if a[i]%2 and not i%2: odds += 1
		elif not a[i]%2 and i%2: evens += 1
	if evens - odds == 0: return min(evens, odds)
	return '-1'

for i in range(t):
    n = input()  # not going to use
    a = [int(j) for j in input().split()]
    print(solve(a))

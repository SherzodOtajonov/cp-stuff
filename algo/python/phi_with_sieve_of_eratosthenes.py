# phi, that is euler's totient function, using Sieve of Eratosthenes. 
def phi(n):
	from math import sqrt
	res = n
	for i in range(2, int(sqrt(n))+1):
		if n%i == 0:
			while n%i == 0:
				n/=i
			res -= res/i
	if n>1:
		res -= res/n
	return res
# smaple: phi(900) -> 240

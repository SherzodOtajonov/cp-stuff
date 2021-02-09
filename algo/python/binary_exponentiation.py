# Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to 
# calculate an using only O(logn) multiplications (instead of O(n) multiplications required by the 
# naive approach).

def binpow(a, b, mod):
    a%=mod
    res=1
    while b:
        if b%2: res = (res*a)%mod
        a = (a*a)%mod
        b=b//2
    return res

print(binpow(2, 704511, 1000000007))  # 852098711

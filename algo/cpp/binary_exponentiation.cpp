// Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to 
// calculate a^n using only O(logn) multiplications (instead of O(n) multiplications required by 
// the naive approach

#include <bits/stdc++.h>
using namespace std;

// a>0, b>=0
long long binpow(long long a, long long b, long long mod) {
    a%=mod;
    long long res = 1;
    while (b) {
        if (b%2) res = res*a%mod;
        a=a*a%mod;
        b/=2;
    }
    return res;
}

int main(){
    // cout<<binpow(2, 704511, 1000000007)<<endl; // 852098711
    return 0;
}

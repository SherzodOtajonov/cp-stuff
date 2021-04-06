// Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to 
// calculate a^n using only O(logn) multiplications (instead of O(n) multiplications required by 
// the naive approach

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ll long long
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()

typedef pair<int, int> pairs;

constexpr int MOD = 1e9+7;

ll mod(ll n, ll m=MOD){n%=m;if(n<0)n+=m;return n;}

// a>0, b>=0
ll binpow(ll a, ll b) {
    a=mod(a);
    ll res = 1;
    while(b) {
        if(b%2) res = mod(res*a);
        a=mod(a*a);
        b/=2;
    }
    return res;
}

int main(){

    return 0;
}

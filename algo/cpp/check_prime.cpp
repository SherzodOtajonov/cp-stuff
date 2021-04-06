#include "bits/stdc++.h"
using namespace std;

#define endl '\n'
#define ll long long
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()

typedef pair<int, int> pairs;

constexpr int MOD = 1e9+7;

ll mod(ll n, ll m=MOD){n%=m;if(n<0)n+=m;return n;}


bool prime(ll x) {
    if(x == 1) return false;
    if(x == 2) return true;
    if(x == 3) return true;
    if(x % 3 == 0 || x % 2== 0) return false;
    
    for(ll i = 5; i * i <= x; i += 6) {
        if(x % i == 0 || x % (i+2) == 0)return false;
    }
    return true;
}

int main(){
    ios_base::sync_with_stdio(false), cin.tie(nullptr);

	return 0;
}

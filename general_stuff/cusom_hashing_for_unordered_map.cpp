#include "bits/stdc++.h"
using namespace std;
 
#define endl '\n'
#define ll long long
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()

typedef pair<int, int> pairs;
 
constexpr int MOD = 1e9+7;
 
ll mod(ll n, ll m=MOD){n%=m;if(n<0)n+=m;return n;}


struct custom_hash {
	// neal's custom hash for unordered_set
	// link to blog: https://codeforces.com/blog/entry/62393
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
	// unordered_map<long long, int, custom_hash> safe_map;
	// gp_hash_table<long long, int, custom_hash> safe_hash_table;

};

int main(){
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int t=1;// cin>>t;
	while(t--) solve();
	return 0;
}

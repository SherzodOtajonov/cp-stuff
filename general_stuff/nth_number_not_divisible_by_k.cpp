#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ll long long
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()

constexpr int MOD = 1e9+7;

int main(){
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
	
	ll n, k, x; cin>>n>>k;
	x = n/(k-1);
	ll res=x*(k-1);
	for(ll i=x*k; i<x*k+k; i++){
		if(res==n) {
			cout<<i-1<<endl; return 0;
		}
		if(i%k) res++;
	}
    return 0;
}

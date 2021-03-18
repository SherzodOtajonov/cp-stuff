#include <bits/stdc++.h>
using namespace std;
 
#define ll long long
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
 
 
constexpr int MOD = 1e9+7;
 
 
void solve(){
	int n, k, x, y, m, r1, r2; cin>>n;
	vector<int> a(n);
	for(int i=0; i<n; i++) cin>>a[i];
	sort(all(a));
	cin>>k;
	for(int i=0; i<k; i++){
		cin>>x>>y;
		
		// find smllest i such that a[i] >= x
		int l=-1, r=n;
		while(l+1<r){
			m = (l+r)/2;
			if(a[m]<x) l=m;
			else r=m;
		}
		r1=r;
		
		// find largest i such that a[i] <= y
		l=-1; r=n;
		while(l+1<r){
			m = (l+r)/2;
			if(a[m]<=y) l=m;
			else r=m;
		}
		r2=l+1;
		cout<<r2-r1<<endl;
	}
}
 
int main() {
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	
	int t=1; //cin>>t;
	while(t--) solve();
}

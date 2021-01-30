#include <bits/stdc++.h>

using namespace std;

void solve(){
	long long n, k;
	cin>>n>>k;
	long long x = (n+k-1)/k;
	x*=k;

	cout <<(x+n-1) / n<<endl;
}


int main(){
	int t;
	cin>>t;
	for(int i; i<t; i++)
		solve();
	return 0;
}

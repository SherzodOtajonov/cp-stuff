#include <bits/stdc++.h>
using namespace std;
 
void solve(){
	int n, a=0, b=0, c=0, t; cin>>n;
	for(int i=0; i<n; i++){
		cin>>t;
		if (t%3==0) a++;
		else if (t%3==1) b++;
		else c++;
	}
	n/=3;
	int r=0;
	
	for(int i=0; i<2; i++){
		if(a>n){ r+=(a-n); b+=(a-n); a=n;}
		if(b>n){r+=(b-n); c+=(b-n); b=n;}
		if (c>n){ r+=(c-n); a+=(c-n); c=n;}
	}
	cout<<r<<endl;
}
 
int main(){
	int t; cin>>t;
	while(t--) solve();
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(){
	long long n, s, d, x, y;
	cin>>n>>s>>d;
	for (long long i=0; i<n;i++){
		cin>>x>>y;
		if (x<s && y>d){
			cout<<"YES"<<endl;
			return 0;
		}
	}
	cout<<"NO"<<endl;
	return 0;
}

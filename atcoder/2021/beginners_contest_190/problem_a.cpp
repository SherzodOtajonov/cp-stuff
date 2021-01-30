#include <bits/stdc++.h>

using namespace std;

int main(){
	int a, b, c;
	cin>>a>>b>>c;
	if (a==b){
		if (c==0) cout<<"Aoki"<<endl;
		else cout<<"Takahashi"<<endl;
	} else if (a>b) cout<<"Takahashi"<<endl;
	else cout<<"Aoki"<<endl;
	return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main(){
	int n, c, r=0, j=0; cin>>n;
	for(int i=0; i<n; i++){
		cin>>c;
		if (c==-1){
			if(j) j--;
			else r++;
		} else j+=c;
	}
	cout<<r<<endl;
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(){
	int a, b;
	cin>>a>>b;
	string x, y, z;
	x.resize(b);
	y.resize(b);
	z.resize(b);
	for (int i=0;i<b;i++){
		x[i] = '#';
		if (i==0){
			y[i]='#';
			z[i]='.';
		} else if (i==b-1){
			y[i]='.';
			z[i]='#';
		} else {
			y[i]='.';
			z[i]='.';
		}
	}
	int f=0;
	for (int i=0; i<a; i++){
		if (i%2==0) cout<<x<<endl;
		else if (i%2 && f) {cout<<z<<endl; f=1;}
		else {cout<<y<<endl;f=0}
	}

	return 0;
}

#include <iostream>

using namespace std;

int main() {
	int t, w, h, n;
	cin>>t;
	for (int i=0; i<t; i++) {
		cin>>w>>h>>n;
		int c=1;
		while (w%2==0){
			c*=2;
			w/= 2;
		}
		while (h%2==0) {
			c*=2;
			h/=2;
		}
		if (c >= n)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}

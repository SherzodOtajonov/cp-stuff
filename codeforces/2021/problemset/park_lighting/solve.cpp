#include <iostream>
#include <cmath>

using namespace std;

int main(){
	int t;
	cin>>t;
	long double n, m;
	for(int i=0; i<t; i++){
		cin>>n>>m;
		cout<<(int)ceil(m*n/2)<<endl;
	}
	return 0;
}

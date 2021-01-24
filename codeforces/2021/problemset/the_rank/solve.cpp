#include <iostream>

using namespace std;

int main(){
	int n;
	if (n==1){
		cout<<1<<endl;
		return 0;
	}
	int m, tmp, r, s=1;
	for (int i=0;i<4;i++){
		cin>>tmp;
		m+=tmp;
	}
	for (int i=1; i<n; i++){
		r=0;
		for (int j=0; i<4;j++){
			cin>>tmp;
			r+=tmp;
		}
		if (r>m)
			s+=1;
	}
	cout<<s<<endl;
	return 0;
}

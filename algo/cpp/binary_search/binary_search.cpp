#include <iostream>

using namespace std;

int main() {
	int A[10] = {6, 8, 13, 15, 20, 23, 25, 28, 30, 35};
	int l=0, h=9, m, key;
	cout<<"Enter key: ";
	cin>>key;
	while (l<=h){
		m = (l+h)/2;
		if (key==A[m]){
			cout<<"Found at index "<<m<<endl;
			return 0;
		}
		else if (key<A[m]) h=m-1;
		else l=m+1;
	}
	cout<<"Not found"<<endl;
	return 0;
}


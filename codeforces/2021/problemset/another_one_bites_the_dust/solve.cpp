#include <iostream>
#include <cmath>

using namespace std;

int main() {
	long long int a, b, c;
	cin>>a>>b>>c;
	if (a == b)
		cout<<c*2+a+b<<endl;
	else
		cout<<c*2+min(a, b)*2+1<<endl;
	return 0;
}

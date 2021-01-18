#include <iostream>

using namespace std;

int solve(string s) {
    int l=0, r=0, q=0;
    for (auto x: s){
        if (x == 'R')
            r+=1;
        else if (x == 'L')
            l+=1;
        else
            q+=1;
    }
    return abs(l-r)+q;
}

int main() {
	string s;
	cout<<"Enter a string consisting of letters: L, R or ?: ";
	cin>>s;
	cout<<solve(s)<<endl;
	return 0;
}

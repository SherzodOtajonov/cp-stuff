#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, r=1;
    cin>>n;
    string prev, c;
    cin>>prev;
    for (int i=1; i<n; i++){
        cin>>c;
        if (prev[1] == c[0]) {
            r+=1; prev = c;
        }
    }
    cout<<r<<endl;
    return 0;
}

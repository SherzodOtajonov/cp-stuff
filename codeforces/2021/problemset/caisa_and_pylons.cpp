#include <bits/stdc++.h>
using namespace std;
 
// 1, x-1 always works
int main(){
    int n, c; cin>>n;
    long long r=0, e=0;
    while (n--){
        cin>>c;
        if (c>e){
            r+=c-e; e=c;
        }
    }
    cout<<r<<endl;
}

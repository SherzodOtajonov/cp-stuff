#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int n, a=0, b=0, c; cin>>n;
    for (int i=0; i<n; i++){
        cin>>c;
        if (c>0) a+=c;
        else b+=c;
    }
    cout<<a-b<<endl;
    return 0;
}

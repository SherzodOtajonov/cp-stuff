#include <bits/stdc++.h>
using namespace std;
 
 
int main(){
    string r;
    int l=1, u=1000001, c;
    while(l<u){
        c=(u+l)/2;
        if (u-l==1) break;
        cout<<c<<endl;
        cout.flush();
        cin>>r;
        if (r=="<") u=c;
        else l=c;
    }
    cout<<"! "<<c<<endl;
    return 0;
}

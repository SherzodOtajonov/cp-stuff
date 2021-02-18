#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int n; cin>>n;
    string s="GBIV";
    cout<<"ROYGBIV";
    for (int i=0; i<n-7;i++) cout<<s[i%4];
    return 0;
}

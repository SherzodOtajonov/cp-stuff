#include <bits/stdc++.h>
using namespace std;
 
void solve(){
    int n,x,a,e=0,o=0; cin>>n>>x;
    for(int i=0;i<n;i++){
        cin>>a;
        if(a%2) o++;
        else e++;
    }
    if(o && o%2==0) o--;
    if (!o) cout<<"No"<<"\n";
    else if(x%2){
        cout<<((x-o)<=e ? "Yes":"No")<<"\n";
    } else if(x%2==0) 
        cout<<((e && (x-e)<=o) ? "Yes":"No")<<"\n";
}
 
int main(){
    int t; cin>>t;
    for(int i=0; i<t; i++) solve();
    return 0;
}

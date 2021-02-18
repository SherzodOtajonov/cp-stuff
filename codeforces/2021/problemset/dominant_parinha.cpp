#include <bits/stdc++.h>
using namespace std;
 
int solve(){
    int n, m=0, c; cin>>n;
    int A[n];
    for(int i=0; i<n; i++) {cin>>c; A[i]=c; if(c>m) m=c;}
    for(int i=0; i<n; i++){
        if (A[i]==m){
            if (i==0 && A[i+1]<m) return i+1;
            if (i==n-1 && A[i-1]<m) return n;
            if (i!=0 && i!=n-1 && (A[i+1]<m || A[i-1]<m)) return i+1;
        }
    }
    return -1;
}
 
int main(){
    int t; cin>>t;
    for(int i=0; i<t; i++) cout<<solve()<<"\n";
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int t, n; cin>>t;
    while(t--){
        cin>>n;
        int x=1, r=0, f=0;
        int A[n], B[n];
        for (int i=0; i<n; i++) cin>>A[i];
        for (int i=0; i<n; i++) cin>>B[i];
        for (int i=0; i<n; i++) {
            if (B[i]-A[i]<0) {cout<<"NO"<<endl; x=0; break;}
            else if (B[i]-A[i] !=f && B[i]-A[i]){f=B[i]-A[i]; r+=1;}
            else f=B[i]-A[i];
            if (r>1){ cout<<"NO"<<endl; x=0; break; }
        }
        if (x) cout<<"YES"<<endl;
    }
    return 0;
}

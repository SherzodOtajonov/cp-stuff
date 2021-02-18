#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int t, n, s;
    cin>>t;
    while(t--){
        cin>>n;
        int A[n];
        for(int i=0; i<n;i++) {cin>>A[i]; s+=A[i];}
        if (s==0) cout<<"NO"<<endl;
        else if(s>0){
            cout<<"YES"<<endl;
            sort(A, A+n, greater<int>());
            for (int x: A) cout<<x<<" ";
            cout<<endl;
        } else {
            cout<<"YES"<<endl;
            sort(A, A+n);
            for (int x: A) cout<<x<<" ";
            cout<<endl;
        }
        s=0;
    }
    return 0;
}

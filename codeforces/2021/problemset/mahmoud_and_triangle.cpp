#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin>>n;
    int A[n];
    for (int i=0; i<n; i++){
        cin>>A[i];
    } 
    sort(A, A+n);
    int a, b, c;
    for (int i=0;i<n-2;i++){
        a=A[i]; b=A[i+1]; c=A[i+2];
        if (a<b+c && b<a+c && c<b+a){
            cout<<"YES"<<endl; return 0;
        }
    }
    cout<<"NO"<<endl;
    return 0;
}

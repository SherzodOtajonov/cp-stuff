#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m, a, b;
    long long s1=0, s2=0;
    cin>>n>>m;
    int A[n];
    for (int i=0;i<n;i++){
        cin>>a>>b; s1+=a; s2+=b;
        A[i]=a-b;
    }
    if (s1<=m) cout<<0<<endl;
    else if (s2>m) cout<<-1<<endl;
    else {
        int r=0;
        sort(A, A+n, greater<int>());
        for (int i=0; i<n; i++){
            r+=1; s1-=A[i];
            if (s1<=m){
                cout<<r<<endl;
                return 0;
            }
        }
    }
    return 0;
}

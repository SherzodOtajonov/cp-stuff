#include <bits/stdc++.h>
using namespace std;

int main(){
    int A[7], a, b, c;
    for(int i=0; i<7; i++) cin>>A[i];
    sort(A, A+7);
    a=A[0]; b=A[1];
    c=A[5]-b;
    cout<<a<<" "<<b<<" "<<c<<endl;
    return 0;
}

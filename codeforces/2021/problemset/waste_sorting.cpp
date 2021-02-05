#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    int c1, c2, c3, a1, a2, a3, a4, a5;
    while (t--){
        cin>>c1>>c2>>c3>>a1>>a2>>a3>>a4>>a5;
        if (a1>c1 || a2>c2) cout<<"NO"<<endl;
        else {
            a1+=a4; a2+=a5;
            if (a1>c1) a3+=a1-c1;
            if (a2>c2) a3+=a2-c2;
            if (a3<=c3) cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
    }
    return 0;
}

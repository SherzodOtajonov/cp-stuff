#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, c;
    cin>>n;
    for (int i=0; i<n; i++){
        cin>>c;
        if (c%2==0) cout<<c-1<<endl;
        else cout<<c<<endl;
    }
    return 0;
}

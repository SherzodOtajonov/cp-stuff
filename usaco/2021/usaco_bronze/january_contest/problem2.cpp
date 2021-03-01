#include <bits/stdc++.h>
using namespace std;

int main(){
    int e=0, o=0, c, n; cin>>n;
    
    for(int i=0; i<n; i++){
        cin>>c;
        if(c%2) o++;
        else e++;
    }
    while(o>e){
        o-=2;
        e++;
    }
    if(e>o+1) e=o+1;
    cout<<e+o<<endl;
    return 0;
}

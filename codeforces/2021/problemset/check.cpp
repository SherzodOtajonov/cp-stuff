#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, neg=0, pos=0, c; cin>>n;
    for(int i=0; i<n; i++){
        cin>>c;
        if (c<0) neg++;
        else if (c>0) pos++;
    }
    int cl = (n+2-1)/2; 
    if (neg>=cl) cout<<-1<<endl;
    else if(pos>=cl) cout<<1<<endl;
    else cout<<0<<endl;
    return 0;
}

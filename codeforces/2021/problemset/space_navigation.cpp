#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int t, a, b;
    string s;
    cin>>t;
    while (t--){
        int f=1;
        cin>>a>>b;
        cin>>s;
        for(char x: s){
            if (a<0 && x=='L') a++;
            else if (a>0 && x=='R') a--;
            if (b<0 && x=='D') b++;
            else if (b>0 && x=='U') b--;
            if (a==0 && b==0){ cout<<"YES"<<endl; f=0; break; }
        }
        if (f) cout<<"NO"<<endl;;
    }
}

#include <bits/stdc++.h>
using namespace std;
 
int main(){
   int a, b; cin>>a>>b;
   if (a==1 && b==1) cout<<'='<<'\n';
   else if (a==1) cout<<'<'<<'\n';
   else if (b==1) cout<<'>'<<'\n';
   else{
       if (a<10 && b<10){
           int t=a;
           a=pow(b, a);
           b=pow(t,b);
       }
       if(a<b) cout<<'>'<<"\n";
       else if(a>b) cout<<'<'<<"\n";
       else cout<<'='<<"\n";
   }
    return 0;
}

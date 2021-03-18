#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int n, k; cin>>n>>k;
    vector<int> a(n);
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
 
    for(int i=0; i<k; i++){
        int x;
        cin>>x;
        
        // l < x <= r
        int l=-1, r=n;
        while(l+1 < r){
            int m = (l+r)/2;
            if(a[m] < x) l = m;
            else r = m;
        }
        cout<<r+1<<endl;
    }
    return 0;
}

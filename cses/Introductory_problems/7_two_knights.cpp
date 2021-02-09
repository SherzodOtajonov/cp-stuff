#include <bits/stdc++.h>
using namespace std;

// explanation of solution https://www.youtube.com/watch?v=12Y8OrlRS3U&t=175s

int main(){
    long long n;
    cin>>n;
    for(long long i=1; i<=n; i++){
        long long t = (i*i)*(i*i-1)/2;
        long long a = 4*(i-1)*(i-2);
        cout<<t-a<<endl;
    }
    return 0;
}

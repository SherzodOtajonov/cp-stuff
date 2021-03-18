// https://cp-algorithms.com/string/manacher.html

#include <bits/stdc++.h>
using namespace std;

#define all(a) a.begin(), a.end()

void manacher(string s, int n){
    // palindromes with odd length
    // if the length of a palindrome is x, its stored as (x+1)/2 in d[i]
    vector<int> d1(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
        int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
        while (0 <= i - k && i + k < n && s[i - k] == s[i + k]) {
            k++;
        }
        d1[i] = k--;
        if (i + k > r) {
            l = i - k;
            r = i + k;
        }
    }

    // palindromes with even length
    // if the length of a palindrome is x, its stored as x/2 in d[i]
    vector<int> d2(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
        int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
        while (0 <= i - k - 1 && i + k < n && s[i - k - 1] == s[i + k]) {
            k++;
        }
        d2[i] = k--;
        if (i + k > r) {
            l = i - k - 1;
            r = i + k ;
        }
    }
   int a=0, b=0;
   for(int x: d1){
       if(a<x) a=x;
   }
   for(int x: d2){
       if(b<x) b=x;
   }
   // length of the largest polindrome
   cout<<max(a*2-1, b*2)<<endl;
}

int main(){
    //length of the string
    int n; cin>>n;
    string s; 
    cin>>s;
    manacher(s, n);
}

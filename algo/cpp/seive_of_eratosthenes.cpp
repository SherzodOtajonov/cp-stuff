// sourse: https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html

#include <bits/stdc++.h>
using namespace std;

#define ll long long

vector<ll> primes;
void seive(int n){
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i)
                is_prime[j] = false;
        }
    }
    for(int i = 0; i < n; i++){
        if(is_prime[i]) primes.push_back(i); 
    }
}

int main(){
    int n; cin >> n;
    seive(n);
    for(ll x: primes) cout << x << " ";
    return 0;
}

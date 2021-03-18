// code by maksim1744

#include "bits/stdc++.h"
using namespace std;

struct FactMaker {} S;
long long operator * (long long x, const FactMaker &s) {
    long long res = 1;
    for (int i = 1; i <= x; ++i)
        res *= i;
    return res;
}

#define F * S


int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    long long k = 8 F; // one way of using: 8th factorial
    cout << k << endl;

    long long x = 5;
    cout << x F << endl; // another way: 5th factorial
    return 0;
}

// s`ourse: https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
vector<int> seive(int n) {     
    vector<char> A(n+1, true);
    A[0] = A[1] = false;
    for (int i = 2; i <= n; i++) {
        if (A[i] && (long long)i * i <= n) {
            for (int j = i * i; j <= n; j += i)
                A[j] = false;
        }
    }
    vector<int> r;
    for (int i=0; i<is_prime.size();i++){
        if (is_prime[i]) r.push_back(i);
    }
    return r;
}



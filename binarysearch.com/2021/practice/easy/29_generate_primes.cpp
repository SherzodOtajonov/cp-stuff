vector<int> solve(int n) {     
    vector<char> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i] && (long long)i * i <= n) {
            for (int j = i * i; j <= n; j += i)
                is_prime[j] = false;
        }
    }
    vector<int> r;
    for (int i=0; i<is_prime.size();i++){
        if (is_prime[i]) r.push_back(i);
    }
    return r;
}

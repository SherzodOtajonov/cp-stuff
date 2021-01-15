// amstrong number are the ones whose sum of every digits^3 is equal to itself
// e.g. 153 is an amstrong number because 1^3+5^3+3^3 is equal ot 153.
bool amstrong_number(int n){
    int r, tmp=n;
    while (tmp>0){
        r+=pow(tmp%10, 3);
        tmp/=10;
    }
    return r == n;
}

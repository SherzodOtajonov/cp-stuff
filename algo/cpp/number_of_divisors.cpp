// algo to find the number of divisors of a number n in O(sqrt(n)) time
int number_of_divisors(int n) {
    int c=0;
    for(int i=1;i<=sqrt(n); ++i) {
        if(n%i == 0){
                if(i == n/2)
                    c++;
                else
                    c+=2;
        };
    }
    return c;

}

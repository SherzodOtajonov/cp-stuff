class Solution:
    def solve(self, n):
        n = bin(n)
        r=c=0
        for i in range(len(n)):
            if n[i] == '1':
                c+=1
            if n[i] != '1' or (n[i] == '1' and i == len(n)-1):
                r = max(r, c)
                c=0
        return r
        

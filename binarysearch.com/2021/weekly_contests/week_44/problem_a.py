class Solution:
    def solve(self, s):
        l = []
        c=''
        for i in range(len(s)):
            if s[i].isdigit(): c+=s[i]
            if not s[i].isdigit() or (s[i].isdigit() and i==len(s)-1):
                if c:
                    l.append(int(c))
                    c=''
        return sum(l)

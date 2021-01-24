class Solution:
    def solve(self, s):
        r =  []
        for i in range(len(s)):
            n = ''
            while s[i].isdigit():
                n += s[i]
                i+=1
            if n:
                for x in range(int(n)):
                    r.append(s[i])
        return ''.join(r)

class Solution:
    def solve(self, s):
        if not s: return ''
        r=[s[0]]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                r.append(s[i])
        return ''.join(r)

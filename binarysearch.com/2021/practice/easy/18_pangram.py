from string import ascii_lowercase as al
class Solution:
    def solve(self, s):
        r=0
        l=[]
        for i in s:
            if i.lower() in al and i.lower() not in l:
                r+=1
                l.append(i.lower())
        return r==26

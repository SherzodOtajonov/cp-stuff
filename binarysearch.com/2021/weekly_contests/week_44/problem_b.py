class Solution:
    def solve(self, s):
        l=[]
        c=0
        for i in s:
            if i == '(': 
                c+=1
                if c>len(l):
                    l.append(0)
            elif i==')': c-=1
            else: l[c-1]+=1
        return l

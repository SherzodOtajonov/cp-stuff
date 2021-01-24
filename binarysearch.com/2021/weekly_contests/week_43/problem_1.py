class Solution:
    def solve(self, contacts):
        if not contacts: return 0
        r=1
        f=1
        s = set(contacts[0])
        for i in range(1, len(contacts)):
            for j in contacts[i]:
                if j in s:
                    f=0
                s.add(j)
            if f:
                r+=1
            else: f=1
        return r

class Solution:
    def solve(self, lists):
        r = []
        for i in lists:
            for j in i:
                r.append(j)
        return sorted(r)

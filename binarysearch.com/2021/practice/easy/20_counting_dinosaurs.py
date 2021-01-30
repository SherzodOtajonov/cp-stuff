from collections import Counter
class Solution:
    def solve(self, animals, dinosaurs):
        r=0
        c=Counter(animals)
        for i in set(dinosaurs):
            r+= c[i]
        return r

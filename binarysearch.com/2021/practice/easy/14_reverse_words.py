class Solution:
    def solve(self, sentence):
        l = sentence.split(' ')
        l.reverse()
        return ' '.join(l)

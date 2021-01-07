class Solution:
    def solve(self, stacks):
        if not stacks: return 0
        for i in stacks:
            for j in range(1, len(i)):
                i[j] = i[j-1]+i[j]
        for i in range(len(stacks[0])-1, -1, -1):
            if all(map(lambda x: stacks[0][i] in x, stacks[1:])):
                return stacks[0][i]
        else:
            return 0

class Solution:
    def solve(self, s):
        stack = []
        for i in s:
            if i == '(': stack.append(i)
            else:
                if not stack: return False
                else: stack.pop()
        return not len(stack)

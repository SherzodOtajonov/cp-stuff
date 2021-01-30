class Solution:
    def solve(self, moves, x, y):
        t=[0,0]
        for i in moves:
            if i == 'NORTH':
                t[0]+=1
            elif i == 'SOUTH':
                t[0]-=1
            elif i == 'WEST':
                t[1]-=1
            else:
                t[1]+=1
        return [y,x] == t

"""
ID: thisiso1
LANG: PYTHON2
TASK: test
"""

a=b=0
with open('test.in') as f:
    a, b = map(int, f.readline().split())

with open('test.out', 'w') as f:
    f.write(str(a+b)+'\n')

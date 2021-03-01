import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
inp = lambda : input().decode()
print = lambda x: sys.stdout.write(str(x) + '\n')
intmap = lambda : map(int, inp().split(' '))
int_lst = lambda : list(map(int, inp().split(' ')))

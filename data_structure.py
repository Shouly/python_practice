# list tuple dict set
import os

l = []
print(len(l))
l.append(6)
print(len(l))
print(l)  # 1,2,3,4,5,6
l.insert(9, 7)
print(l.pop())
print(l.index(6))

print('--------tuple--------')
t = ()
print(len(t))
t = (1, 23)
print(t)

print('--------dict--------')
d = {'k1': 1, 'k2': 2, 1: 10, 1: 11}
print(d)
print(d['k1'])
print(d[1])

print('--------set--------')
s = set(t)
print(s)

print('-------------------')
L = (1, 2, 3, 2, 5, 6, 788, 8)
L1 = [1, 2, 3, 4, 5]
print(L[0:3])
print(L1[0:3])
print(L[:8])
print(L[-2:-1])
print(L[-2:])
L = list(range(10))
print(L)
print(L[0:10:2])
print(L[::2])
print(L[:])
print(L[-2:])
print(L[-2::])
print(L[-2::1])

print(L[-2::-1])
print(L[-2::-2])
print([x for x in os.listdir('/')])
L = ('a1', 2, 3, 2, 5, 6, 788, 8)
print(list([x.upper() for x in L if isinstance(x,str)]))
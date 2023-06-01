a = set([1,2,3,4,5])
b = set([2,4])
a = a-b
print(type(a))
print(a)


lost = [0,1,2,3]
reserve = [1,2,3,4]

_lost = [l for l in lost if l not in reserve]
_reserve = [r for r in reserve if r not in lost]
print(_lost)
print(_reserve)
from itertools import permutations
from itertools import combinations
from itertools import product

items = ['1','2','3','4','5','6','7']
a = list(permutations(items,2))
b = list(combinations(items,2))
print(a)
print()
print(b)


a = [1,2,3,4,5,6]
b = ['a','b','c','d','e','f']
print(list(product(a,b,repeat=2)))
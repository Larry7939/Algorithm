#itertools(permutations,combinations,product)
from itertools import permutations
from itertools import combinations
from itertools import product
a = [1,2,3,4]
b = ['a','b','c','d']
print(list(permutations(a,2)))
print(list(combinations(a,2)))
print(list(product(a,b)))

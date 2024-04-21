from collections import Counter
N, M = map(int,input().split())
dnas = []
result = []
x = 0
for _ in range(N):
    dnas.append(list(''.join(input().split())))
for dna in list(zip(*dnas)):
    a = Counter(sorted(dna)).most_common(1)[0]
    x += N - a[1]
    result.append(a[0])
print(''.join(result))
print(x)
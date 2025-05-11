s = input()
a = []
for i in s:
    a.append(int(i))
a.sort(reverse=True)
result = a[0]

for i in range(1,len(a)):
    if a[i] > 1:
        result = result * a[i]
    else:
        result = result + a[i]
print(result)
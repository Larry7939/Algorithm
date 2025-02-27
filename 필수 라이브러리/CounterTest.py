from collections import Counter
a = [1,1,1,2,2,2,2,4,4,4,3,4]
print("Counter")
counter = Counter(a)
print(f"4의 등장 횟수 = {counter[4]}")

print(f"최빈값 및 등장 횟수 = {Counter(a).most_common(1)[0]}")
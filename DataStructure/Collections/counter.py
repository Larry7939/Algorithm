from collections import Counter

#list, tuple 등을 Counter Dictionary로 바꾸어 주는 클래스이다. 
# 인자로 받은 배열의 각 값이 몇 개 있는지 반환한다.
lst = [1,1,2,2,2,2,1,2,2,22,3,3,3,3,33,3,4,4,4,4]
counter = Counter(lst)
print(counter)
print(counter.most_common(1)) #가장 많이 포함된 원소 및 개수 반환



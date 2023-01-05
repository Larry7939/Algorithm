from operator import itemgetter
# 리스트에 비해 원소 삽입, 삭제, 검색에 매우 용이하다!
# 1. 인덱스값을 숫자가 아닌 문자열을 쓰고싶을 때
# 2. 빠른 검색, 탐색이 필요할 때
# 3. 집계가 필요할 때(collection 모듈의 Counter 클래스 활용해서 원소의 개수 세기!)

# Init
dict1 = dict()
Dog = {'name': '동동이',
       'weight': 4,
       'height': 100
       }
# dict를 value로 하는 경우
Animal = {
    'Dog': {
        'name': '동동이',
        'weight': 4,
        'height': 100
    },
    'Cat': {
        'name': '야옹이',
        'age': 5
    }
}

# Get
dict2 = {'하이': 300, '헬로': 180, 3: 5}
dict2['하이']  # 300
dict2.get('동동', 0)  # 0 key(동동)가 없을 때에는 0을 가져온다.

# Set
dict3 = {'김철수': 300, 'Anna': 100}
dict3['홍길동'] = 200
dict3['김철수'] = 200  # 수정 가능
dict3['김철수'] += 200  # 수정 가능

# Delete
dict4 = {'김철수': 300, 'Anna': 180}
del dict4['김철수']
# del dict4['홍길동'] #key error 발생
dict4.pop('김철수', 180)  # 김철수가 없으면 디폴트값 180, 있으면 김철수 삭제하고 300반환

# Iterate
dict5 = {'김철수': 300, 'Anna': 180}
for key in dict5:  # key 순회
    print(key)
for key, value in dict5.items():  # key-value 동시 순회
    print(key, value)

# 특정 키 포함여부 검사 in
print('김철수' in dict5)
print('홍길동' in dict5)

# key 또는 value, 둘 다 뽑아내기
print(list(dict5.keys()))
print(list(dict5.values()))
print(list(dict5.items()))

# 정렬
dic = {
    1: 'b',
    3: 'c',
    5: 'd',
    4: 'a',
    2: 'e'
}
dic_keys = sorted(dic.keys())
dic_values = sorted(dic.values())
dic_items = sorted(dic.items())  # key를 기준으로 정렬된 리스트가 튜플 형태로 반환
# 내림차순 정렬
dic_keys = sorted(dic.keys(), reverse=True)

# value 기준 정렬
dic = {
    1: 'b',
    3: 'c',
    5: 'd',
    4: 'a',
    2: 'e'
}
dic_key_sorted = sorted(dic.items(), key=lambda item: item[0])
dic_value_sorted = sorted(dic.items(), key=lambda item: item[1])

#sorted와 itemgetter를 이용하여 정렬하기
student = [
    {'name':'park','age':10},
    {'name':'lee','age':43},
    {'name':'kim','age':20},
    {'name':'Amy','age':20},
    {'name':'choi','age':5},
]
#age로 오름차순 정렬 한 상태를 유지하고 name으로 오름차순 정렬하기
stu_sorted = sorted(student,key = itemgetter('age','name')) #Amy와 kim처럼 나이가 같은 경우 Amy가 더 앞에 오게 된다.
print(stu_sorted)
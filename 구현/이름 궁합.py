# BOJ 15312 이름 궁합
import sys
sys.setrecursionlimit(10000)

# 배열과 배열의 길이를 매개변수로 하는 함수
# 배열을 돌며, 1부터 시작해, 직전 원소와 더한 다음 새로운 배열에 넣고, 마지막에 반환하는 동작
# 재귀로 동작
alphabets = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1,
             'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}


def recur_name_compatibility(arr):
    n = len(arr)
    result = []
    for i in range(1, n):
        result.append(arr[i-1] % 10+arr[i] % 10)
    if len(result) == 2:
        result = list(map(lambda x: x%10,result))
        answer = list(map(str,result))
        print(''.join(answer))
    else:
        recur_name_compatibility(result)


name1 = sys.stdin.readline().rstrip()
name2 = sys.stdin.readline().rstrip()
j = 0
k = 0
length = len(name1+name2)
name = []

for pair in zip(name1,name2):
    name.append(alphabets[pair[0]])
    name.append(alphabets[pair[1]])

recur_name_compatibility(name)
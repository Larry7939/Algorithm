#BOJ 1181 단어 정렬
import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(sys.stdin.readline().strip())#개행문자를 없애주기 위해 strip()추가
a = list(set(a))
a = sorted(a,key=lambda x: (len(x),x))#길이를 기준으로 정렬 후, 사전 순 정렬
for i in a:
    print(i)
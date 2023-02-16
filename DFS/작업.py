# BOJ 21937
# 풀이횟수 2
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**7)

def dfs(v):
    global answer
    visited[v]=1
    for i in graph[v]:
        if visited[i] == 0:
            answer +=1
            dfs(i)

#입력부
#작업 개수(N), 순서 정보 개수(M)
N,M = map(int,input().split())
visited = [0]*(N+1)
answer = 0
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[y].append(x)

#목적지 입력
v = int(input())

dfs(v)
print(answer)

# 컴퓨터 수 N
# 컴퓨터 쌍의 수 M
# 각 컴퓨터 번호를 인덱스로 하는 리스트에 연결된 컴퓨터를 append한다.
# dfs 함수에서 만약 인자를 타고 오는 infected 리스트에 False라고 되어있는 경우에 한해서만 dfs를 재귀호출한다.
# 만약 인자로 전달된 것의 infected가 True인 경우 return
# False인 경우 True로 변경

def dfs(computers, v):
    if infected[v] == True:
        return
    infected[v] = True
    for computer in computers[v]:
        dfs(computers, computer)

N = int(input())
M = int(input())    
computers = [[] for _ in range(N+1)]
infected = [False]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    computers[a].append(b)
    computers[b].append(a)
answer = 0
dfs(computers, 1)
print(infected.count(True)-1)
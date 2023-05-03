# 바이러스, 작업, 촌수 계산, 헌내기는 친구가 필요해, 섬의 개수, 음료수 얼려먹기, 사과빨리먹기, 컴백홈

# 입력
#  컴퓨터의 수 - N
#  컴퓨터 쌍의 수 - M
#  컴퓨터 번호 쌍 M개 -  길이 N의 배열 relationships[]
# 출력
#  1번 컴퓨터와 직간접적으로 연결되어있는 컴퓨터의 수 - result

# 컴퓨터 연결하는 방법
#  각 컴퓨터 n의 관계를 나타내는 relationships[n]에 연결하고 싶은 컴퓨터 번호를 append한다.
#  위 과정은 M번 수행된다.
def addRelation(currentComputer:int,computerNumber:int):
    relationGraph[currentComputer].append(computerNumber)
    relationGraph[computerNumber].append(currentComputer)


#1번부터 시작해서 연결되어있는 컴퓨터 번호로 이동하고 result를 증가시킨다.
#다시 돌아오지 않도록 visited[i]가 False인지를 검사한다.
def DFS(v):
    global result
    visited[v] = True
    for i in relationGraph[v]:
        if(visited[i]==False):
            result += 1
            DFS(i)

N = int(input())
M = int(input())
relationGraph = [[] for _ in range(N+1)]
result = 0
start = 1
visited = [False]*(N+1)
for _ in range(M):
    x,y = map(int,input().split())
    addRelation(x,y)
DFS(start)
print(result)
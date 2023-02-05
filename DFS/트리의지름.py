#BOJ 1167 트리의 지름

#입력부
#트리의 정점의 개수 V입력
graph = [[] for _ in range(V)]
#V개의 간선 정보 입력

visited = [False]*(V+1)
#dfs
def dfs(v,diameter): #정점과 지름
    visited[v] = True
    for i in graph[v]:
        diameter
        dfs(i)
#graph[v] - 정점 v의 간선 정보:List
#graph[v] -> i[1:-2] -> a-> 정점v와 -1을 뺀 순수 (정점,거리) 리스트
#a-> for(i in range(0,len(a),2)):
#       a[i],a[i+1]
#

#출력부
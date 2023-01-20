vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]
def dfs(start,graph=set(),visited=set()):
    if start not in visited:
        graph.clear()
        visited.add(start) #visited에 start를 추가
        print(vertex[start],end=' ') #vertex[start]를 출력
        for j in range(len(vertex)): 
            if adjMat[start][j]==1: #adjMat[start]][0~7]까지를 검사해서 1인 정점들, 즉 인접정점을 검사한다.
                graph.add(j) #이렇게 하면, graph에는 인접정점들이 모이게된다.
        nbr = graph-visited #{인접정점} - {방문정점}
        for v in nbr:
            dfs(v,graph,visited)
start_vertex = input("시작 지점을 입력하세요: ")
dfs(vertex.index(start_vertex))

# dfs(adjMat,'A')
# #start를 숫자로 하면,
# #graph[A]에서 visited = {'A'}를 뺀다.
# adjMat[0][1] # 이건 B랑
# adjMat[0][2] # 이건 C랑
#graph[start]가 인접정점이다.
#visited에는 {'A','B','C'}이런 식으로 들어갈거임.
#graph[]에는 한 행만 읽어서 
#visited = {'B','C'}
#graph = {}
#인접 정점은, adjMat에서 1인 애들을 말하는 것임.
#A의 인접 정점은 adjMat[0][1],agjMat[0][2]임. 1이니까.
#즉, start를 기준으로 해서 인접 정점을 계산해서(1인 애들을 모아서) visited로 차집합을 하면 된다.
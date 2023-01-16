import queue
q = queue.Queue()
vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]
def bfs(start,graph=set(),visited=set()):
    q.put(start)
    visited.add(start) #start는 방문한 정점임.
    while not q.empty():#큐가 비어있지 않는 동안 진행
        graph.clear()
        start = q.get()
        print(vertex[start],end=' ') #vertex[start]를 출력
        for j in range(len(vertex)): 
            if adjMat[start][j]==1: #adjMat[start]][0~7]까지를 검사해서 1인 정점들, 즉 인접정점을 검사한다.
                graph.add(j) #이렇게 하면, graph에는 인접정점들이 모이게된다.
        nbr = graph-visited #{인접정점} - {방문정점}
        for v in nbr:
            visited.add(v) #visited에 v를 추가
            q.put(v) #v를 큐에 삽입
start_vertex = input("시작 지점을 입력하세요: ")
bfs(vertex.index(start_vertex))

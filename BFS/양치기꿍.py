#이중for문을 돌면서 .인 경우에만 bfs 호출
#nx,ny조건을 나눌 때, graph[ny][nx]가 #이 아닐 때에만 bfs(nx,ny)를 호출할 수 있도록 함.
#한 번 호출될 때마다 while문이 끝날 때 변수 k와 v를 비교해서 작은 것은 0으로 만들기

R,C = map(int,input().split())
graph = []
for _ in range(R):
    a = list(input())
    graph.append(a)
    print(a)


for i in range(R):
    for j in range(C):
        print(graph[i][j],end='')
    print()
    
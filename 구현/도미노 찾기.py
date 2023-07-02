#BOJ 1553 도미노 찾기
import sys
# 총 28가지의 도미노
# 도미노의 크기 - 1X2
# 도미노는 회전이 가능하다.
# 같은 도미노를 여러 번 사용할 수 없다.
# 격자에는 0부터 6까지의 수만 존재한다.

graph = []
for i in range(8):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
visited = [[False]*7 for _ in range(8)]
dominos = [[False]*7 for _ in range(7)]

# 매 칸마다 좌표상 도미노가 들어갈 수 있는지, 이미 사용된 도미노가 아닌지, 비어있는 칸인지를 체크한다.

def rec_fun(x,y):
    if y == 8: return 1 #탐색 완료
    count = 0
    nx,ny = x+1,y #오른쪽으로 이동
    if nx == 7: #오른쪽 끝이라면 개행
        nx,ny = 0,y+1

    if visited[y][x]: #오른쪽 칸으로 이동
        return rec_fun(nx,ny)
    
    else: #도미노 사용
        now = graph[y][x]
        visited[y][x] = True
        for dx,dy in ((0,1),(1,0)): #아래와 오른쪽 확인
            mx,my = x+dx, y+dy
            if mx in range(7) and my in range(8):
                pair = graph[my][mx] #아래나 오른쪽 값
                if not visited[my][mx] and not dominos[now][pair]: #놓을 수 있고, 사용되지 않은 도미노
                    dominos[now][pair] = dominos[pair][now] = True #도미노 사용 처리
                    visited[my][mx] = True #방문 처리

                    count += rec_fun(nx,ny) #다음 위치로 이동

                    visited[my][mx] = False # 도미노의 pair를 놓은 위치를 백트래킹 해주기 위함.
                    dominos[now][pair] = dominos[pair][now] = False #백트래킹
        visited[y][x] = False #도미노의 now를 놓은 위치를 백트래킹 해주기 위함. 이렇게 해줘야 최초에 아래로 놓은 도미노를 없애고, 오른쪽으로 도미노를 놓을 수 있다.
        return count

print(rec_fun(0,0))

# 백트래킹으로 앞전 시행 결과가, 현재 시행 결과에 영향을 미치지 않도록 구현하는 것이 핵심
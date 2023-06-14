#프로그래머스 - 자물쇠와 열쇠
# 키가 자유롭게 이동할 수 있도록 공간 확보 & 키를 돌리는 동작을 구현하는 것이 핵심

# 확장된 공간의 중심에 lock을 배치한 board 만들기    
def createBoard(M,N,lock):
    board = [[0]*(M*2+N) for _ in range(M*2+N)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    return board
# 키 돌리기 로직
def rotate90Key(key):
    return list(zip(*key[::-1]))
# 키 체크 로직 - key와 lock의 각 원소를 더한 결과, 하나라도 1이 아니라면, return False
def check(M,N,board):
    for i in range(M,M+N):
        for j in range(M,M+N):
            if board[i][j] != 1:
                return False
    return True 
# 키 넣기 로직 - key와 lock의 각 원소를 더하기
# 이미 lock은 board의 중앙에 있으니, key만 더하면 된다.
def attach(x,y,M,key,board):
    for i in range(M):
        for j in range(M):
            board[y+i][x+j] += key[i][j]
            
# 키 빼기 로직 - lock의 각 원소에서 key의 각 원소를 빼기    
def detach(x,y,M,key,board):
    for i in range(M):
        for j in range(M):
            board[y+i][x+j] -= key[i][j] 
            
def solution(key, lock):
    # 키가 자유롭게 이동할 수 있도록 공간 확보 & 키를 돌리는 동작을 구현하는 것이 핵심
    M,N = len(key),len(lock)
    
    board = createBoard(M,N,lock)
    
    for _ in range(4):
        key = rotate90Key(key)
        for x in range(M+N+1):
            for y in range(M+N+1):
                attach(x,y,M,key,board)       
                if check(M,N,board):
                    return True
                detach(x,y,M,key,board)
    return False
    
#메인 로직 - 외부 반복 : 돌리기, 내부 반복 : 돌려진 키로 키 넣기, 체크, 빼기 로직 호출하기
#체크 결과 True가 나오면 return True, False면 빼기로직 호출
#외부 반복문 밖에 return False
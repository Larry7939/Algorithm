# n 입력
n = int(input())
logicDict = dict()

# key is value의 형태로 dict에 삽입
# 위 과정을 n회 반복
for _ in range(n):
    start, end = input().split(" is ")
    if start not in logicDict:
        logicDict[start] = []
        
    logicDict[start].append(end)

def dfs(start, end):
    if start == end:
        return True
    if start not in logicDict:
        return False
    visitedDict.add(start)
    for s in logicDict[start]:
        if s not in visitedDict:
            if dfs(s, end):
                return True
    return False

# m 입력
# dfs 호출 출발지와 목적지 각각 p,q를 인자로 전달
# 위 과정을 m회 반복
result = []
m = int(input())
for _ in range(m):
    s,e = input().split(" is ")
    visitedDict = set()
    result.append(dfs(s,e))

for r in result:
    if r:
        print('T')
    else:
        print('F')

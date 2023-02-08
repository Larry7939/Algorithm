parent = []
set_size = 0
#총 6개의 vertice가 있다는 가정
#nSets에는 set의 개수가 들어감.
def init_set(nSets):# 각 부모노드를 전부 -1로 초기화한다.
    global set_size,parent #set_size랑 parent 전역변수를 함수 안에서도 사용하겠다.
    set_size = nSets
    for i in range(nSets):
        parent.append(-1) #부모노드는 전부 -1로 초기화한다. 1,2,3~6까지 다 -1임.
        #슬라이드에서 설명했듯이, 부모노드는 전부 -1로 잡는데, 1,4를 합치면 4의 parent는 -1이고, 1의 parent는 4가 되는 것이다.
def union(s1,s2): #두개의 집합을 합친다고 하면, set_size를 하나 줄여야한다.
    global set_size
    set_size = set_size-1
    parent[s1] = s2
def find(id): #어떤 id를 갖고있는 노드의 최상위 부모인 root를 찾는다.
    while(parent[id]>=0): #특정 id를 갖고있는 노드의 값이 -1이 아닌동안, 즉, root가 아닌동안
        id= parent[id] #계속 위로 올라가는 거다.
    return id
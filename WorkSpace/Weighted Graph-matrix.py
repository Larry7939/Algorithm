#Weighted Graph
vertex = ['A','B','C','D','E','F','G'] #정점들
weight = [[None,29,None,None,None,10,None], #A는 B랑 F랑만 연결되어있음. 각각 가중치는 29랑 10임.
          [29,None,16,None,None,None,15],
          [None,16,None,12,None,None,None],
          [None,None,12,None,22,None,18],
          [None,None,None,22,None,27,25],
          [10,None,None,None,27,None,None],
          [None,15,None,18,None,25,None],
]
graph = (vertex,weight) #weight를 통해서 연결되었는지의 여부를 알 수 있다.
def WeightSum(vlist,W): #정점리스트와 인접행렬
    sum =0
    for i in range(len(vlist)):
        for j in range(i+1,len(vlist)): #무방향그래프이기 때문에, 대각선을 기준으로 한쪽 삼각형에 있는 가중치만 더하면 된다.
            if W[i][j] != None:
                sum+= W[i][j]
    return sum
print("AM: weight sum = ",WeightSum(vertex,weight))
def printAllEdges(vlist,W): #정점리스트와 인접행렬
    for i in range(len(vlist)):
        for j in range(i+1,len(vlist)): 
            if W[i][j] != None:
                print("(%s,%s,%d)"%(vlist[i],vlist[j],W[i][j]),end=' ') #모든 간선을 출력한다.
    print()
printAllEdges(vertex,weight)
graph = {'A':set([('B',29),('F',10)]), #각각의 튜플로 구성된 리스트가 집합화된다.
         'B':set([('A',29),('C',16),('G',15)]),
         'C':set([('B',16),('D',12)]),
         'D':set([('C',12),('E',22),('G',18)]),
         'E':set([('D',22),('F',27),('G',25)]),
         'F':set([('A',10),('E',27)]),
         'G':set([('B',15),('D',18),('E',25)])
}
#graph의 'A'를 key값으로 해서 접근하면, 'B','F'간선에 접근할 수 있다.
#앞서 했던 가중치 합이랑 간선구하는 함수를 똑같이 구현해보자.
def weightSum(graph): #각 간선에 접근하는 방법을 익혀보자.
    sum =0
    for v in graph: #각 key값으로 순회하면서,
        for e in graph[v]: #각 key값으로 얻을 수 있는 graph내의 정보들 순회. 여기에서 e는 각 튜플들이다.
            sum += e[1] #각 튜플들 내에서 index 1번째에 있는 가중치를 더한다.
    return sum//2 #중복돼서 더해지는 것들 제하기 위해 2로 나눈다.

def printAllEdges(graph):
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)"%(v,e[0],e[1]),end=' ')
print("AM: weight sum = ",weightSum(graph))
printAllEdges(graph) #총 18개의 edge가 나온다.
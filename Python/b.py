# A공용 주차장은 일반적인 주차장과는 다른 특이한 형태로, 이진 트리 모양을 하고있다.
# 이 주차장에서 주차 공간은 이진트리의 각 노드로 표현되며, 간선을 따라 주차공간 사이를 이동할 수 있다.
# 각 주차 공간에는 차는 1대씩 주차할 수 있으며, 이미 차가 주차된 주차 공간은 다른 차가 지나갈 수 없습니다.
# 주차장의 입구와 출구는 루트노드로 표현되는 주차공간에 있다.
# 모든 주차공간이 빈 A공용 주차장에 자동차 두 대를 주차하려 한다.
# 단, 어느 한 자동차를 운전해서 주차장 밖으로 나가려 할 때, 다른 자동차 한 대가 방해되지 않아아야한다.
# 주차장의 형태를 나타내는 이진트리가 담긴 배열 parking이 매개변수로 주어진다. 어느 한 자동차를 운전해서 주차장 출구로 나가려할 때, 다른 자동차 한 대가 방해받지 않도록 자동차 두 대를 주차하는 방법의 개수를 return하도록 solution 함수를 작성하라.

# 주차공간을 나타내는 노드 개수가 N개일 때, 각 주차 공간에는 0부터 N-1까지 번호가 하나씩 붙어있다.
# parking은 이진트리가 담긴 이차원 배열 형태이다.
# parking의 i번째 행은 i번 노드의 [왼쪽 자식 노드번호, 오른쪽 자식 노드 번호]이다. 행은 0번 행부터 N-1번 행까지 있다.
# 해당 위치에 자식 노드가 없는 경우 -1이 담겨있다.
# parking의 행 길이(전체 노드 개수)는 3이상 200,000이하이다.
# 이진트리의 루트 노드는 항상 0번 노드이다.
# 따라서 주차장의 입구, 출구는 항상 0번 노드이다.
# 0번 노드에서 출발한 자동차가 도달할 수 없는 노드는 없다.
# 만약 자동차를 주차할 수 있는 방법이 없다면 0을 return한다.

# 입출력 예시1
# parking = [[1,2],[3,4],[-1,-1],[-1,-1],[-1,-1]]
# result = 4
# 입출력 예시2
# parking = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# result = 26

# 키 포인트: 모든 노드에 대해 자식을 모두 갖고 있는 노드에 한하여 양쪽 서브트리 노드의 수를 곱하여 합산한다.

# 시간 복잡도: O(N^2)
def solution(parking):
    from collections import defaultdict
    answer = 0
    # 트리 구조를 나타내는 딕셔너리 생성
    tree = defaultdict(list)
    
    # 트리를 구성하기 위한 각 노드의 자식 정보를 추가 -> 모든 노드를 한 번씩 방문하므로 O(N)
    for i, (left, right) in enumerate(parking):
        if left != -1:
            tree[i].append(left)
        else:
            tree[i].append(None)
        if right != -1:
            tree[i].append(right)
        else:
            tree[i].append(None)

    for key in tree.keys():
        # 좌우 자식을 모두 갖고있는 노드에 한하여 좌우 서브트리의 노드 수 합산 -> 각 노드에 대해 count_subtree_node 함수를 호출하므로 O(N^2)
        if tree[key][0] != None and tree[key][1] != None:
            left_subtree_count = count_subtree_node(tree, tree[key][0])
            right_subtree_count = count_subtree_node(tree, tree[key][1])
            answer += left_subtree_count * right_subtree_count
    return answer

# 재귀호출로 매개변수로 주어진 node를 부모 노드로 하는 서브트리의 노드 수 합산 -> 최악의 경우 모든 노드를 한 번씩 방문하므로 O(N)
def count_subtree_node(tree, node):
    if node is None:
        return 0
    left_count = count_subtree_node(tree, tree[node][0])
    right_count = count_subtree_node(tree, tree[node][1])
    
    total = left_count + right_count + 1
    return total



# 입출력 예시1
parking = [[1,2],[3,4],[-1,-1],[-1,-1],[-1,-1]]

print(solution(parking))
# 입출력 예시2
parking = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
print(solution(parking))
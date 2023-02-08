class TNode:
    def __init__(self,data,left,right):
        self.data =data
        self.left = left
        self.right = right
def preorder(n): 
    if n is not None:
        print(n.data,end=' ')#전위순회는 루트부터 순회한다.
        preorder(n.left)
        preorder(n.right)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data,end=' ')
        inorder(n.right)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data,end=' ')
def count_node(n): #노드의 개수
    #터미널 노드는 left,right가 0이기 때문에, left,right에 대해서 count_node함수를 호출하면 0이 return되기 때문에,
    #터미널 노드는 자기 자신만 1이 return 된다.
    if n is None:return 0
    else: return 1 + count_node(n.left)+count_node(n.right) #계속해서 자기자신 + 왼쪽 + 오른쪽, 결국 전위 순회방법으로 count하는 것임.
def count_leaf(n):
    if n is None:return 0
    elif n.left is None and n.right is None: return 1 #n.left랑 n.right가 둘 다 None이면 return 1
    else: return count_leaf(n.left) + count_leaf(n.right) # 다 끝나고 나면, count를 left랑 right를 더해준 값을 반환한다. 
    #루트노드에 대한 연산이 어디에 들어가도 되기 때문에, 순회방법은 상관없다.
def calc_height(n): #루트에서부터 left,right해서 쭉 내려가기 때문에, 전위순회라고 볼 수 있다.
    if n is None: return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft>hRight:
        return hLeft+1
    else:
        return hRight+1

d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',f,None)
root = TNode('A',b,c)
print("전위 순회")
preorder(root)
print()
print("중위 순회")
inorder(root)
print()
print("후위 순회")
postorder(root)
print()
print("Node의 개수 = %d개"%count_node(root))
print("단말의 개수 = %d개"%count_leaf(root))
print("트리의 높이 = %d"%calc_height(root))
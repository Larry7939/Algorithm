class BSTNode:
    def __init__(self,key,value):
        self.key =key
        self.value=value
        self.left =None
        self.right=None
def search_bst(n,key):
    if n==None: 
        return None
    elif key == n.key:
        return n
    elif key<n.key:
        return search_bst(n.left,key)
    else:
        return search_bst(n.right,key)
#반복구조 ver.
# def search_max_bst(n):
#     while n!=None and n.right!=None:
#         n=n.right
#     return n
# def search_min_bst(n):
#     while n!=None and n.left!=None:
#         n = n.left
#     return n
#순환구조 ver.
def search_max_bst(n):
    if n.right==None:
        return n
    else:
        return search_max_bst(n.right)
def search_min_bst(n):
    if n.left==None:
        return n
    else:
        return search_min_bst(n.left)
#순환구조 ver.
def insert_bst(r,n):
    if n.key<r.key: #만약 넣으려고 하는 노드의 key값이 r의 key값보다 작으면
        if r.left is None:#왼쪽으로 간다. 가다가 None이 나오는 위치에 삽입한다.
            r.left =n
            return True
        else:
            return insert_bst(r.left,n) #None이 나오기 전까지, r.left를 r로 해서 계속 탐색한다.
    elif  n.key>r.key: #만약 넣으려고 하는 노드의 key값이 r의 key값보다 크면
        if r.right is None:#오른쪽으로 간다. 가다가 None이 나오는 위치에 삽입한다.
            r.right =n
            return True
        else:
            return insert_bst(r.right,n) #None이 나오기 전까지, r.right를 r로 해서 계속 탐색한다.
    else: #만약에 같으면?? BST에서는 유일한 KEY값을 갖기 때문에, 집어넣을 수가 없다.
        return False
#반복구조 ver.
# def insert_bst(r,n):
#     while True:
#         if n.key<r.key:
#             if r.left==None:
#                 r.left = n
#                 return True
#             else:
#                 r=r.left
#         elif n.key>r.key:
#             if r.right==None:
#                 r.right = n
#                 return True
#             else:
#                 r=r.right
#         else:
#             return False
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key,end=' ')
        inorder(n.right)
    
#BST에 insert할 때는 루트노드가 있는 상태라고 가정하기 때문에, 루트노드는 18로 만들어진 상태라고 생각하고, 7,26,3,12,31,9,27을 넣어보자.
data = [7,26,3,12,31,9,27]
root = BSTNode(18,'A') #루트노드를 만든 다음에 계속 삽입해보자.
for key in data:
    n = BSTNode(key,'A') #'A'는 그냥 더미값임
    insert_bst(root,n)
    inorder(root)
    print()
#지난 시간에 배운 중위순회를 적용해보자.
#중위순회를 해보면 정렬된 결과가 나오는 것을 볼 수 있다.
#BST의 큰 특징은, 중위순회를 하면, 정렬된 결과를 볼 수 있다는 것이다.

#search를 해볼 수도 있다.
print(search_bst(root,26).key)
#없는건 search가 안된다. None반환.
# print(search_bst(root,32).key)

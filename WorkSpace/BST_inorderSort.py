class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left=None
        self.right=None
def insert_bst(r,n):
    if r.key<n.key:
        if r.right == None:
            r.right = n
        else:
            insert_bst(r.right,n)
    elif r.key>n.key:
        if r.left==None:
            r.left =n
        else:
            insert_bst(r.left,n)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key,end=' ')
        inorder(n.right)
NumArray = [11,3,4,1,56,5,6,2,98,32,23]
root = BSTNode(NumArray[0]) #배열 NumArray의 첫번째 원소를 root노드로 정함.
for i in NumArray:
    n = BSTNode(i)
    insert_bst(root,n)
inorder(root)

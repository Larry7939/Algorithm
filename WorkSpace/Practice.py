class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left =None
        self.right =None
def search_bst(n,key):
    if n==None:
        return None
    elif key==n.key:
        return n
    elif key<n.key:
        search_bst(n.left,key)
    else:
        search_bst(n.right,key)
def search_max_bst(n):
    while n!=None and n.right!=None:
        n = n.right
    return n
def search_min_bst(n):
    while n!=None and n.left!=None:
        n = n.left
    n.left = n
def insert_bst(r,n):
    if r.key>n.key:
        if r.left is None:
            r.left = n
        else:
            insert_bst(r.left,n)
    elif r.key<n.key:
        if r.right is None:
            r.right =n
        else:
            insert_bst(r.right,n)
    else:
        return False

    
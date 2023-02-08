class ArrayList:
    def __init__(self):
        self.items = []
    def insert(self,pos,elem):
        self.items.insert(pos,elem)
    def delete(self,pos):
        return self.items.pop(pos)
    def isEmpty(self):
        return self.size()==0
    def getEntry(self,pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.top = []
    def find(self,item):
        return self.items.index(item)
    def replace(self,pos,elem):
        self.items[pos]=elem
    def sort(self):
        self.items.sort()
    def merge(self,lst):
        self.items.extend(lst)
    def display(self,msg='ArrayList:'):
        print(msg,'항목수=',self.size(),self.items)
def multPoly(Poly1,Poly2):
    mPoly=[0]*(Poly1.size()+Poly2.size()-1)
    for i in range(Poly1.size()):
        for j in range(Poly2.size()):
            mPoly[i+j]+=Poly1.getEntry(i)*Poly2.getEntry(j)
    print(mPoly)
Poly1 = ArrayList()
Poly2 = ArrayList()
Poly1.insert(0,1)
Poly1.insert(1,2)
Poly1.insert(2,0)
Poly1.insert(3,1)
Poly2.insert(0,2)
Poly2.insert(1,1)
multPoly(Poly1,Poly2)

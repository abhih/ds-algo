#create a node first and then put it in linkedlist

class Node(object):
    def __init__(self,data,nextnode =None):
        self.data=data
        self.nextnode=nextnode
    def get_nextnode(self):
        return self.nextnode
    def get_data(self):
        return self.data
    def set_next(self,node):
        self.nextnode=node
    def set_data(self,data):
        self.data=data
        
class LinkedList(object):
    def __init__(self):
        self.head=None

ll=LinkedList()
A=Node("A")
B=Node("B")
C=Node("C")
ll.head=A
A.nextnode=B
B.nextnode=C

for i in range(3):
    print(ll.head.data)
    ll.head=ll.head.nextnode
    

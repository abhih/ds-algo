class Tree(object):
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if not self.data:
            self.data=data
        else:
            if data<self.data:
                if self.left is None:
                    self.left=Tree(data)
                else:
                    self.left.insert(data)
            else:
                if data > self.data:
                    if self.right is None:
                        self.right=Tree(data)
                    else:
                        self.right.insert(data)
    def get_tree(self):
        if self.left:
            print("On left")
            (self.left.get_tree())
        print(self.data)
        if self.right:
            print("On right")
            (self.right.get_tree())
root=Tree(20)
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.get_tree()
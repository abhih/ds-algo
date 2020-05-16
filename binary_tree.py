class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
count=10
class BinarySearchTree(object):

    def __init__(self):
        self.root=None

    def insert(self,root,node):
        if isinstance(node,Node):
            if node.data < root.data:
                if root.left is None:
                   root.left=node
                else:
                    self.insert(root.left,node)
            elif node.data > root.data:
                if root.right is None:
                   root.right=node
                else:
                    self.insert(root.right,node)
        return
    # def insert(self,node):
    #     if isinstance(node,Node):
    #         if node.data < self.root.data:
    #             if self.root.left is None:
    #                self.root.left=node
    #             else:
    #                 self.root=self.root.left
    #                 self.insert(node)
    #         elif node.data > self.root.data:
    #             if self.root.right is None:
    #                self.root.right=node
    #             else:
    #                 self.root=self.root.right
    #                 self.insert(node)

    def inorder(self,root):
        if root:
            (self.inorder(root.left))
            print(root.data)
            (self.inorder(root.right))
        
        
    def search(self,root,data):
        self.root=root
        if self.root==None or self.root.data==data:
            return self.root
        elif self.root.data<data:
            self.search(self.root.left,data)
        elif self.root.data>data:
            self.search(self.root.right,data)

    def get_child(self,node):
        self.inorder(node)
    def delete(self,node):
        if node.left is None or node.right is None:
            node=None
        
A0=Node(50)
A=Node(30)
B=Node(20)
C=Node(40)
D=Node(70)
E=Node(60)
F=Node(80)

bst=BinarySearchTree()
root=bst.root=A0
bst.insert(root,A)
bst.insert(root,B)
bst.insert(root,C)
bst.insert(root,D)
bst.insert(root,E)
bst.insert(root,F)
bst.inorder(root)
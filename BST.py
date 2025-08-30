class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def__init__(self):
        self.root=None
    def insert(self,value):
        if self.root=None:
            self.root=Node(value)
        else:
            self.ins_rep(self.root,value)
    def ins_rep(self,current,value):
        if value<current.value:
            if current.left==None:
                current.left=value
            else:
                self.ins_rep(current.left,value)
        elif value>current.value:
            if current.right==None:
                current.right=value
            else:
                self.ins_rep(current.right,value)

N1=Node(15)
BST1=BST()
BST1.insert(15)
A=[15,8,20,5,17]


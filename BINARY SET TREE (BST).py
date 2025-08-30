class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self.ins_rep(self.root,value)
    def ins_rep(self,current,value):
        if value<current.value:
            if current.left==None:
                current.left=Node(value)
            else:
                self.ins_rep(current.left,value)
        elif value>current.value:
            if current.right==None:
                current.right=Node(value)
            else:
                self.ins_rep(current.right,value)
        self.find(self.root,value)
    
    def find(self,current,value):
        if current==None:
            return None
        if value==current.value:
            return current
        if value<current.value:
            return self.find(current.left,value)
        else:
            return self.find(current.right,value)

N1=Node(15)
BST1=BST()
A=[15,8,20,5,17]
for i in A:
    BST1.insert(i)
found_node=BST1.find(BST1.root,17)
if found_node:
    print(found_node)
else:
    print("value not found")


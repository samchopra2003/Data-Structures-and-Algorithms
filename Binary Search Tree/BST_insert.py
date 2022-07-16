class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self): # no arguments required to create empty BST
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value: # a tree must have unique values
                return False
            if new_node.value < temp.value: # lesser values to the left
                if temp.left is None: # empty position
                    temp.left = new_node
                    return True
                temp = temp.left
            else:                           # greater values to the right
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
            
                

        


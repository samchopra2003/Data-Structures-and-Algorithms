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

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:      # lesser values to the left
                temp = temp.left
            elif value > temp.value:    # greater values to the right
                temp = temp.right
            else:
                return True
        return False

    def min_val_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def BFS(self): # Breadth First Search
        current_node = self.root
        queue = []  # list not the data structure queue
        results = [] 
        queue.append(current_node)

        while len(queue) > 0:   # when queue is empty while loop will break
            current_node = queue.pop(0) # first item popped off and added to results 
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_pre_order(self):
        results = []

        def traverse(current_node): # recursion- call stack
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def DFS_in_order(self):
        results = []

        def traverse(current_node): 
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) # order changed again 
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.DFS_in_order()) # results list should be in ascending order
            
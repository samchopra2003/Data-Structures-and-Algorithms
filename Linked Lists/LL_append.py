class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self): 
        temp = self.head
        while temp is not None:
            print(temp.value, end =" ") # Print on the same line
            temp = temp.next

    def append(self, value): # Append method
        new_node = Node(value)
        if self.length == 0: # Edge case(no nodes present in linked list)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()

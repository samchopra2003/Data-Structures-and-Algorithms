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

    def append(self, value): 
        new_node = Node(value)
        if self.length == 0: # Edge case(no nodes present in linked list)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0: # Edge case(no nodes present)
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0: #Edge case (initially one node, after decrementing no nodes remaining)
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0: #Edge case (no nodes present)
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0: # Edge case (no nodes present)
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: #Edge case (initially one node, after decrementing no nodes remaining)
            self.tail = None
        return temp.value    # .value only for testing

my_linked_list = LinkedList(2)
my_linked_list.append(1)

# 2 items - returns 2 node
print(my_linked_list.pop_first())

# 1 item - returns 1 node
print(my_linked_list.pop_first())

# 0 items - returns none
print(my_linked_list.pop_first())


        







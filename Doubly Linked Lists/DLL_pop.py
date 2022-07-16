class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end= ' ')
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: # Edge case(no nodes present)
            return None
        temp = self.tail
        if self.length == 1: # More readable way to write code rather than pop method in LL
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

# 2 items - returns 2 node
print(my_doubly_linked_list.pop())

# 1 item - returns 1 node
print(my_doubly_linked_list.pop())

# 0 items - returns none
print(my_doubly_linked_list.pop())


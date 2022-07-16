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
        return temp

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
        return temp

    def get(self, index):
        if index < 0 or index >= self.length: #testing whether index is within bounds of LL
            return None
        temp = self.head        
        for _ in range(index): #underscore used when no var is being iterated
            temp = temp.next
        return temp    

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length: # testing whether index is within bounds of LL
            return False
        if index == 0: # prepending
            return self.prepend(value)
        if index == self.length: # appending
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1) # pointing to new node
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length: # testing whether index is within bounds of LL
            return None
        if index == 0: # removing first node
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()






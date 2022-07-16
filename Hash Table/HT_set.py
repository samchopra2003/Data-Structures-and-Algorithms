class HashTable:
    def __init__(self, size = 7): # default size is 7
        self.data_map = [None] * size # creates list with size number of items

    def __hash(self, key): # hash method
        my_hash = 0        # resetting my_hash value
        for letter in key: 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # outputs 0-6 remainder
        return my_hash     # perfect for size 7 (0-6) list 

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] # creates empty list at index
        self.data_map[index].append([key, value])

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()
        

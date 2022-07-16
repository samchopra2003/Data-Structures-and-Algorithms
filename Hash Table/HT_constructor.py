class HashTable:
    def __init__(self, size = 7): # default size is 7
        self.data_map = [None] * size # creates list with size number of items

    def __hash(self, key): # hash method
        my_hash = 0
        for letter in key: 
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # outputs 0-6 remainder
        return my_hash     # perfect for size 7 (0-6) list 

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()
 
my_hash_table.print_table()
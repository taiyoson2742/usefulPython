#written 11-9-26
#A hash table with chaining.
class Hashtable:
    """A Hashtable class implementation."""

    def __init__(self, size = 11):
       '''Sets the data attributes of the hash table.'''
       self.table = [[] for i in range(size)]
       self.__size = size
       self.__items = 0

    def is_empty(self):
        ''' Returns True if the hash table is empty.'''
        return not any(self.table)

    def __len__(self):
        ''' Returns the number of items in the hash table.'''
        return self.__items

    @property
    def size(self):
        ''' Returns a size of the hash table.'''
        return self.__size

    def hash(self, key):
        ''' Returns a hash code as an integer for an ASCII string only.'''
        n = 0
        key = str(key)
        for i in range(len(key)):
            n += ord(key[i])
        return n % self.__size

    def get(self, key):
        ''' Returns the value of a key.'''
        h = self.hash(key)
        for item in self.table[h]:
            if item[0] == key:
                return item[1]
        return None

    def add(self, key, value):
        ''' Adds an item to the hash table.'''
        ### YOUR SOLUTION HERE
        h = self.hash(key)
        for item in self.table[h]:
            if item[0] == key:
                self.remove(key)
                self.table[h].append((key, value))
                break
        else:
            self.table[h].append((key, value))
            self.__items += 1

    def remove(self, key):
        ''' Removes an item from the hash table.'''
        ### YOUR SOLUTION HERE
        h = self.hash(key)
        for item in self.table[h]:
            if item[0] == key:
                self.table[h].remove(item)
                self.__items -= 1
                return

touhous = ['Nazrin', 'Reimu', 'Marisa', 'Reisen', 'Yachiye', 'Suwako',
          'Aya', 'Yuuma', 'Biten', 'Minoriko', 'Auun', 'Yuyuko']

# create a hash table with key-value pairs: 'Nazrin': 1, 'Reimu': 2, 'Marisa': 3, etc.
h = Hashtable()
for i in range(len(touhous)):
    h.add(touhous[i], i+1) # a key is touhous[i], a value is i+1

# print the hash table items
for key in touhous:
    print(key, h.get(key))
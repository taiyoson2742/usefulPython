#written 11.10.26

#implementation of stack, probably already done for you in most cases
#below is the palindrome finder
import copy
class Stack:
    '''Implementation of a stack.'''

    def __init__(self):
        '''Initialization of a stack.'''
        self.__items = []

    @property
    def items(self):
        '''Returns the stack property items.'''
        return self.__items

    def __repr__(self):
        '''Returns a representation of the stack.'''
        return repr(self.__items)

    def isempty(self):
        '''Returns True if the stack is empty. Otherwise, returns False.'''
        return self.__items == []

    def push(self, item):
        '''Adds an item to the top of the stack.'''
        self.__items.append(item)

    def pop(self):
        '''Removes an item from the top of the stack. If there is no item, returns None.'''
        if len(self.__items) == 0:
            return None
        return self.__items.pop()

    def peek(self):
        '''Returns an item at the top of the stack without removing it from the stack.'''
        if len(self.__items) == 0:
            return None
        return self.__items[len(self.__items)-1]

    def size(self):
        '''Returns the number of items in the stack.'''
        return len(self.__items)

    def copy(self):
        '''Returns a deep copy of the stack.'''
        return copy.deepcopy(self)

def is_palindrome(word):
    stack = Stack()

    # fill the stack
    for char in word:
            stack.push(char)
    # create the reversed word
    reverse = ""
    while not stack.isempty():
            reverse += stack.pop()
    return word == reverse


print(is_palindrome("tacocat"))
print(is_palindrome("racecar"))
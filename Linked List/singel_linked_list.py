'''
A Linked list is a 
'''
from typing import Literal

# Node


class Node:
    '''
    node to 
    '''

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# Single Linked List


class SingleList:
    '''
    Single List
    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data, index=None):
        '''
        add
        '''
        node = Node(data)
        if index is None:  # add to the list if there are no elment in it
            if self.head is None:
                self.head = node
                self.tail = node
                self.size += 1
            else:  # adds to the tail
                self.tail.next = node
                self.tail = node
                self.size += 1
        else:
            if index == 0:
                node.next = self.head
                self.head = node
                self.size += 1
            elif index == (self.size - 1):
                self.tail.next = node
                self.tail = node
                self.size += 1

            else:  # adding to specified index
                current = self.head
                previous = self.head
                current_pointer_index = 0
                while current:
                    if index == current_pointer_index:
                        node.next = current
                        previous.next = node
                        self.size += 1
                        return
                    previous = current
                    current = current.next
                    current_pointer_index += 1
                print("The index is out of bounds")

    def trasveral(self):
        '''
        trasveral
        '''
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def list_size(self):
        '''
        retrun the size of list
        '''
        return self.size

    def seacrh(self, data):
        '''
        search for a data
        '''
        current = self.head
        while current:
            if data == current.data:
                return True
            else:
                current = current.next
        return False

    def remove(self, data, node_pos: Literal['first', 'last', None]):
        '''
        removes
        '''
        match node_pos:
            case 'first':
                
        

# TEST CASES
sample = ['ladi', 'liver', 'cool', 'breeze', 'nice', 'cat', 'dog']
Singlelist = SingleList()
for word in sample:
    Singlelist.add(word)

for letter in Singlelist.trasveral():
    print(letter)
print(Singlelist.list_size())

Singlelist.add('Make', 3)
Singlelist.add('out', 5)

for letter in Singlelist.trasveral():
    print(letter)
print(Singlelist.list_size())

for letter in Singlelist.trasveral():
    print(letter)
print(Singlelist.list_size())

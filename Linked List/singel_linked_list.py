'''
A Linked list is a data structure. It consist of chaining nodes that contains data 
and pointers sequentially. Thereby linking them all together
It uses the pointers to point to the next node. 
It's fast in inserting and deleting at either head or tail of the linked list
'''
from typing import Literal  # ex

class Node(object):
    '''
    A node to contain the data and pointer
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleList(object):
    '''
    A Single Linked List
    '''
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def insert(self, data, index=None):
        '''
        For inserting data to the Linked list
        It takes in data and an index, and insert the data at the given index
        If index is None, it insert the data at the end of the Linked List
        '''
        node = Node(data)  # creates a node with the data
        if index is None:
            if self._head is None:  # insert the node as the head if there are no element in it
                self._head = node
                self._tail = node
                self._size += 1
            else:                   # insert the node at the tail of the Linked List
                self._tail.next = node
                self._tail = node
                self._size += 1
        else:                       # if an index is given
            if index == 0:          # if index is the head, then it insert the node at the head
                node.next = self._head
                self._head = node
                self._size += 1
            elif index == (self._size - 1): # if index is the tail, then it insert the node at the tail
                self._tail.next = node
                self._tail = node
                self._size += 1

            else:                   # adding to specified index
                current = self._head
                previous = self._head
                current_pointer_index = 0
                while current:
                    if index == current_pointer_index:
                        node.next = current
                        previous.next = node
                        self._size += 1
                        return
                    previous = current
                    current = current.next
                    current_pointer_index += 1
                print("The index is out of bounds")

    def iter(self):
        '''
        it iterate the linked list and 
        '''
        current = self._head
        while current:
            value = current.data
            current = current.next
            yield value

    def ___size__(self):
        '''
        returns the size of linked list
        '''
        return self._size

    def search(self, data):
        '''
        Search for a data in the linked list and return True if found
        else it return false
        '''
        current = self._head
        while current:
            if data == current.data:
                return True
            else:
                current = current.next
        return False

    def delete(self, data, node_pos: Literal['first', 'last', None]):
        '''
        removes
        '''



# TEST CASES
def test_cases():
    '''
    test case
    '''
    sample = ['ladi', 'liver', 'cool', 'breeze', 'nice', 'cat', 'dog']
    single_list = SingleList()
    for word in sample:
        single_list.insert(word)

    for letter in single_list.iter():
        print(letter)
    print(single_list._size())

    single_list.insert('Make', 3)
    single_list.insert('out', 5)

    for letter in single_list.iter():
        print(letter)
    print(single_list._size())

    for letter in single_list.iter():
        print(letter)
    print(single_list._size())

test_cases()

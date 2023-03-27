'''
A Linked list is a 
'''

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

    def remove(self, data):
        '''
        removes
        '''
        current = self.head
        previous = self.head
        while current:
            if current.data == data:
                current = current.next
                previous.next = current
                self.size -= 1
                return
            previous = current
            current = current.next
        print('Data not in list')


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

Singlelist.remove('ot')

for letter in Singlelist.trasveral():
    print(letter)
print(Singlelist.list_size())


# DOUBLE LINKED LIST


class DoubleListNew:
    '''
    explain double
    '''

    def __init__(self):
        '''
        explain
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data, index=None):
        '''
        explain
        '''
        node = Node(data)
        if index is None:
            if self.head is None:
                self.head = node
                self.tail = node
                self.size += 1
            else:

                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.size += 1
        elif index == 0:
            current_head = self.head
            current_head.prev = node
            node.next = current_head
            self.head = node
            self.size += 1

        elif index == (self.size - 1):
            current_tail = self.tail
            current_tail.next = node
            node.prev = current_tail
            self.tail = node
            self.size += 1

        else:
            current_pointer = self.head.next
            previous_pointer = self.head
            current_pointer_index = 1
            while current_pointer:
                if index == current_pointer_index:
                    previous_pointer.next = node
                    node.prev = previous_pointer
                    node.next = current_pointer
                    current_pointer.prev = node
                    self.size += 1
                    return
                else:
                    previous_pointer = current_pointer
                    current_pointer = current_pointer.next
                    current_pointer_index += 1
            print('Out of bound')

    def seacrh(self, data):
        '''
        search
        '''
        current = self.head
        while current:
            if data == current.data:
                return True
            else:
                current = current.next
        return False

    def list_size(self):
        '''
        size
        '''
        return self.size

    def trasvesral(self):
        '''trasversal'''
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def reversal(self):
        '''
        rev
        '''
        current_tail = self.tail
        while current_tail:
            value = current_tail.data
            current_tail = current_tail.prev
            yield value

    def remove(self, data=None, node_position= 'None'):
        '''
        remove
        '''
        assert node_position in ['first', 'last', 'None']

        if node_position == 'first':
            current_head = self.head
            self.head = current_head.next
            self.size -= 1
        elif node_position == 'last':
            current_tail = self.tail
            self.tail = current_tail.prev
            self.size -= 1
        else:
            current_pointer = self.head
            previous_pointer = self.head
            while current_pointer:
                if current_pointer.data == data:
                    next_node = current_pointer.next
                    next_node.prev = current_pointer.prev
                    previous_pointer.next = current_pointer.next
                    self.size -= 1
                    return
                else:
                    previous_pointer = current_pointer
                    current_pointer = current_pointer.next
            print('Data not in list')


# TEST CASE AREA
sample = ['dipo', 'james', 'simi', 'ladi', 'biggie', 'tupac']
Doublelist = DoubleListNew()
for name in sample:
    Doublelist.add(name)

for name in Doublelist.trasvesral():
    print(name)
print(Doublelist.list_size())

Doublelist.add('begin', index=0)
Doublelist.add('two', index=2)
Doublelist.add('three', index=4)
Doublelist.add('six', index=6)
Doublelist.add('nine', index=9)

for name in Doublelist.trasvesral():
    print(name)

print(Doublelist.list_size())

print(Doublelist.seacrh('ladi'))
print(Doublelist.seacrh('ladipo'))

Doublelist.remove(node_position='first')
Doublelist.remove(node_position='last')
Doublelist.remove('two')
Doublelist.remove('begin')
Doublelist.remove('three')

for name in Doublelist.trasvesral():
    print(name)

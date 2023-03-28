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

    def remove(self, data=None, node_position='None'):
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
    # bug to be fixed        print('Data not in list')


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

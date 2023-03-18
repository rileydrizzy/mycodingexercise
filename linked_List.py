# write introduction to linked list
#Talk about the Big O notation in respect to the key operation of a data structure (reading, searching, insertion, deletion)
# list the advantages and disadvantages of linked list with example of areas of used
# do the same for Double Linked List, Circual Linked List



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class SingleLinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.sizelen = 0

    def append(self, newdata, pos= None):
         if pos == None:
            node = Node(newdata)
            self.Tail 






















# Test cases
def test_case(Node):
    Node('Spam')
    Node('Eggs')
    Node('Ham')

#test_case(Node)

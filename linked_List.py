# write introduction to linked list
#Talk about the Big O notation in respect to the key operation of a data structure (reading, searching, insertion, deletion)
# list the advantages and disadvantages of linked list with example of areas of used
# do the same for Double Linked List, Circual Linked List



class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class SingleLinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.sizelen = 0

    def append(self, newdata, index = None):
        
        if index == None:
            new_node = Node(newdata)
            if self.Tail:
                self.Tail.next = new_node
            else:
                self.Tail, self.Head = new_node
            self.sizelen += 1
    elif:


current_index = 0 
while current_index != index:
    






















# Test cases
def test_case(Node):
    len
    Node('Spam')
    Node('Eggs')
    Node('Ham')
        
#test_case(Node)

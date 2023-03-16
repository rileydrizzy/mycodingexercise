
#

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

"""_summary_
"""
# Stack Implementation with ARRAY

class StackArray:
    """_summary_
    """
    def __init__(self, size) -> None:
        self.size = size
        self.array = [0] * self.size
        self.top = -1
        self.len_ = 0

    def peek(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self.array[self.top]

    def stack_pop(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        if self.top < 0:
            print("Underflow")
            return None
        item = self.array[self.top]
        self.array[self.top] = 0
        self.top-=1
        self.len_ -= 1
        return item
    def stack_push(self, data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        if self.top >= self.size -1:
            print("Overflow")
        else:
            self.top += 1
            self.array[self.top] = data
            self.len_ += 1

    def __len__(self):
        return self.len_

# Stack Implementation with Linked List

class Node:
    """_summary_
    """
    def __init__(self,data= None) -> None:
        self.data = data
        self.prev = None

class StackLinkeedList:
    """_summary_
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self,data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        item = Node(data)
        if self.head is None:
            self.head = item
            self.tail = self.head
        else:
            item.prev = self.tail
            self.tail = item
        self.size+=1

    def pop(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        if self.head is None:
            print("Stack is empty")
            return None
        item = self.tail.data
        self.tail = self.tail.prev
        self.size-=1
        return item
    def __len__(self):
        return self.size

    def peek(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self.tail.data

element_array = ['james','ladi','water', 'running', 'flow', 'bread','food']

# TEST CASE
#stackarr

stackarray_ = StackArray(size=5)
for word in element_array:
    stackarray_.stack_push(word)
print(stackarray_.peek())
check_array = []
for num in range(7):
    data_ = stackarray_.stack_pop()
    if data_:
        check_array.append(data_)
print(element_array[:5][::-1]== check_array)

stacklist_ = StackLinkeedList()
for word in element_array:
    stacklist_.push(word)
print(len(stacklist_))
print(stacklist_.peek())
check_array_2 = []
for num in range(3):
    check_array_2.append(stacklist_.pop())

print(element_array[-3:][::-1]== check_array_2)
print(stacklist_.peek())
print(len(stacklist_))
print(check_array_2)

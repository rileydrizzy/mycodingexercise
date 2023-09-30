"""_summary_
"""
# Stack Implementation with ARRAY

class Stack:
    """_summary_
    """
    def __init__(self, size) -> None:
        self.size = size
        self.array = [] * self.size
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
        else:
            self.top -= 1
            self.array[self.top] = 0
            self.len_ -= 1
            return self.array[self.top+1]

    def stack_push(self, data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        if self.top >= (self.size - 1):
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
        self.next = None

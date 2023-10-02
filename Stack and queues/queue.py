"""doc
"""

class ListQueue:
    """_summary_
    """
    def __init__(self,size) -> None:
        self._slots = []
        self._size = size
        self._front = self._rear = 0
        self._lenght = 0

    def enqueue(self, data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """
        if self._front >= self._size:
            print("Queue is full")
        else:
            self._slots.append(data)
            self._rear+=1
            self._lenght+=1

    def dequeue(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        if self._front == self._rear:
            print("Queue is empty")
            return None
        else:
            item = self._slots.pop(0)
            self._rear-=1
            self._lenght-=1
            return item

    def peek(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return self._slots[0]

    def __len__(self):
        return self._lenght


class Node:
    """_summary_
    """
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class LinkedListQueue:
    """_summary_
    """
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self,data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        item = Node(data)
        if self._head is None:
            self._head = item
            self._tail = self._head
        else:
            self._tail.next = item
            item.prev = self._tail
            self._tail = item
        self._size+=1

    def dequeue(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        if self._head is None:
            print('Queue is empty')
            return None
        item = self._head.data
        self._head = self._head.next
        self._size-=1
        return item

    def __len__(self):
        return self._size

def test_queue():
    """_summary_
    """
    # Create a new queue
    queue = [ListQueue(3), LinkedListQueue()]
    for my_queue in queue:
        # Enqueue some elements
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)

        # Display the contents of the queue
        #print("Queue elements:", list(my_queue._slots))

        # Dequeue elements
        item1 = my_queue.dequeue()
        item2 = my_queue.dequeue()

        # Display the dequeued elements
        print("Dequeued elements:", item1, item2)

        # Check if the queue is empty
        queue_size = len(my_queue)
        print("Is the queue empty?", queue_size)

if __name__ == "__main__":
    test_queue()

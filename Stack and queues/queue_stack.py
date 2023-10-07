"""doc
"""

class StackQueue:
    """_summary_
    """
    def __init__(self) -> None:
        self._dequeuelist, self._enqueuelist = [],[]
        self._size = 0

    def enqueue(self,data):
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        """
        self._enqueuelist.append(data)
        self._size+=1

    def dequeue(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        if  not self._dequeuelist:
            if  not self._enqueuelist:
                print('Queue is empty')
                return None
            while self._enqueuelist:
                self._dequeuelist.append(self._enqueuelist.pop())

        item = self._dequeuelist.pop()
        self._size-=1
        return item

    def __len__(self):
        return self._size

def test_queue():
    """_summary_
    """
    my_queue = StackQueue()
    my_queue.enqueue(23)
    my_queue.enqueue(13)
    my_queue.enqueue(11)

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
    my_queue.enqueue(32)
    my_queue.enqueue(33)
    my_queue.enqueue(34)
    print(my_queue.dequeue())
test_queue()

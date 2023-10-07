"""doc priorityqueue min heaps
"""

class Node:
    """_summary_
    """
    def __init__(self,data, priority) -> None:
        self.data = data
        self.priority = priority

class PriorityQueueHeap:
    """_summary_
    """
    def __init__(self) -> None:
        self.heap_array = [0]
        self.size = 0

    def insert(self,data, priority)-> None:
        """_summary_

        Parameters
        ----------
        data : _type_
            _description_
        priority : _type_
            _description_
        """
        item = Node(data, priority)
        self.heap_array.append(item)
        self.size+=1
        self._arrange(self.size)

    def _arrange(self,k_idx)-> None:
        while k_idx//2 > 0:
            if self.heap_array[k_idx//2].priority > self.heap_array[k_idx].priority:
                self.heap_array[k_idx//2], self.heap_array[k_idx] =\
                    self.heap_array[k_idx], self.heap_array[k_idx//2]
            k_idx//=2

    def extract(self)-> object:
        """_summary_

        Returns
        -------
        object
            _description_
        """
        item = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()
        self.size-=1
        self._sink(1)
        return item.data, item.priority

    def _sink(self,k_idx)-> None:
        while k_idx*2 <= self.size:
            minichild = self._get_minichild(k_idx)
            if self.heap_array[minichild].priority < self.heap_array[k_idx].priority:
                self.heap_array[minichild], self.heap_array[k_idx] =\
                    self.heap_array[k_idx], self.heap_array[minichild]
            k_idx=minichild

    def _get_minichild(self,k_idx)-> int:
        if k_idx *2+1 > self.size:
            return k_idx *2
        if self.heap_array[k_idx*2].priority < self.heap_array[k_idx*2 +1].priority:
            return k_idx*2
        else:
            return k_idx*2 +1

priorityqueue = PriorityQueueHeap()
array = [(2,'bat'),(13,'Cat'),(18,'Rat'),(26,'Ant'),(3,'Lion'),(4,'Bear') ]
for element in array:
    print(element[1],element[0])
for element in array:
    priorityqueue.insert(element[1],element[0])

for num in range(priorityqueue.size):
    element = priorityqueue.extract()
    print(element)

"""doc min heaps
"""


class MinHeaps:
    """_summary_
    """
    def __init__(self) -> None:
        self.heap = [0]
        self.size = 0

    def insert(self, num):
        """_summary_

        Parameters
        ----------
        num : _type_
            _description_
        """
        self.heap.append(num)
        self.size+=1
        self._arrange(self.size)

    def _arrange(self, k_idx):
        while k_idx // 2 > 0:
            if self.heap[k_idx] < self.heap[k_idx // 2]:
                self.heap[k_idx], self.heap[k_idx //2] = self.heap[k_idx//2], self.heap[k_idx]
            k_idx //= 2

    def extractmin(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -=1
        self._sink(1)
        return item

    def _sink(self,k_idx):
        while k_idx*2 <= self.size:
            minchild = self._get_minichild(k_idx)
            if self.heap[k_idx] > self.heap[minchild]:
                self.heap[k_idx], self.heap[minchild] = self.heap[minchild], self.heap[k_idx]
            k_idx=minchild

    def _get_minichild(self,k_idx):
        if k_idx*2 +1 > self.size:
            return k_idx * 2
        if self.heap[k_idx * 2] < self.heap[k_idx * 2 +1]:
            return k_idx * 2
        else:
            return k_idx * 2 +1

    def heapsort(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        sorted_array = []
        while self.size >= 1:
            item = self.extractmin()
            sorted_array.append(item)
        return sorted_array


array_= [4,8,7,2,9,10,5,1,3,6]
HP = MinHeaps()
for number in array_:
    HP.insert(number)
arr = HP.heapsort()
print(arr)

"""doc max heaps
"""
class MaxHeaP:
    """_summary_
    """
    def __init__(self) -> None:
        self.heap = [0]
        self.size = 0

    def push(self,data):
        self.heap.append(data)
        self.size+=1
        self._arrange(self.size)

    def _arrange(self,k_idx):
        while k_idx //2 < 0:
            if 
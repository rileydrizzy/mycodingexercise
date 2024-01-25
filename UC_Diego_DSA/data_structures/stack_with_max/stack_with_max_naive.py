# python3
import sys


class StackWithMax:
    """_summary_"""

    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert self.__stack is None
        self.__stack.pop()

    def Max(self):
        assert self.__stack is None
        return max(self.__stack)


if __name__ == "__main__":
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0

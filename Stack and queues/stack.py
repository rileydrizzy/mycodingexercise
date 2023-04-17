'''
stack
'''
class Stack:
    def __init__(self, size = None):
        self._sizeof_ = size
        self.data = [0] * (self._sizeof_)
        self.top = -1

    def push(self,x):
        if self.top >= self._sizeof_ - 1:
            print('OverflowError')
        else:
            self.top = self.top +1
            self.data[self.top] = x

    def pop(self):
        if self.top == -1:
            print('Underflow')
        else:
            data = self.data[self.top]
            self.data[self.top] = 0
            self.top = self.top - 1
            return data
    
    def peek(self):
        return self.data[self.top]

#TEST CASE
mystack = Stack(size=4)
sample = ['dad','mom', 'ladi', 'bisy', 'job']
for num in sample:
    mystack.push(num)
print(mystack.peek()) #bisy
print(mystack.pop()) #bisy
print(mystack.peek()) #ladi
print(mystack.pop()) #ladi
print(mystack.peek()) #mom
print(mystack.pop()) #mom
print(mystack.pop()) #dad
print(mystack.pop())  #underflow
print(mystack.peek())
print(mystack.data)
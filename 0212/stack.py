class Stack:
    def __init__(self, capacity= 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity -1

    def push(self,item):
        if self.is_full():
            raise IndexError("Stack is full")
        #데이터를 집어넣었으니 가장 마지막 원소를 가리키는 top 포인터 + 1
        self.top +=1
        self.items[self.top] = item

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        #데이터를 꺼내는 로직
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -=1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[self.top]


stack = Stack(3)
stack.push(3)
stack.push(2)
stack.push(1)

print(stack.pop())
print(stack.pop())
print(stack.pop())

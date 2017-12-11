class StackItem:
    
    def __init__(self, item, head):
        self.item = item
        self.head = head

class Stack:
    _head = None
    _count = 0

    def push(self, item):
        qitem = StackItem(item, self._head)
        self._head = qitem
        self._count += 1

    def pop(self):        
        if self.count() == 0:
            return None

        temp = self._head
        item = temp.item
        self._head = temp.head
        self._count -= 1

        del temp        
        return item

    def clear(self):
        for i in range(self.count()):
            self.pop()

    def count(self):
        return self._count

    def peek(self):
        temp = self._head

        for i in range(self.count()): # Тут у нас не си бл*ть + без массивов
            temp = temp.head
            if i == self.count() - 2: # Maaaagiiiick
                return temp.item


stack = Stack()

stack.push("1")
stack.push("2")
stack.push("3")

# print("Peek: " + str(stack.peek()))
# stack.clear()
print("Count: " + str(stack.count()))

print(stack.pop())
print(stack.pop())
print(stack.pop())

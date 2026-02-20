# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================

# ==================================================
# Stack
# ==================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
    
    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.top is None:
            print('Stack is Empty')
            return None
        else:
            removed_data = self.top.data
            self.top = self.top.next
            return removed_data
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data


    def view(self):
        current = self.top
        print('Top', end=' ' )
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.view()

print('Data terhapus:',s.pop())
s.view
print('Data top:', s.peek())
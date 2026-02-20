# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================

# ==================================================
# Queue
# ==================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        newNode = Node(data)

        if self.is_empty():
            self.front = newNode
            self.rear = newNode
            return
        
        self.rear.next = newNode
        self.rear = newNode
    
    def dequeue(self):
        deletedData = self.front.data
        self.front = self.front.next

    def view(self):
        current = self.front
        print('Front', end=' ')
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print('Rear')
q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.view()
q.dequeue()
q.view()

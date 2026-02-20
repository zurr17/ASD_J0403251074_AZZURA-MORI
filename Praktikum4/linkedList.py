# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================

# ==================================================
# LinkedList
# ==================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')

head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

current = head
while current is not None:
    print(current.data)
    current = current.next

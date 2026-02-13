class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CCL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        if not self.head:
            print('kosong')
            return
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print('null')
    
    def delete(self, key):
        if not self.head:
            return
        temp = self.head
        if temp.data == key:
            if temp.next == self.head:
                self.head = None
                self.tail = None
            else:
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
                self.tail = temp
            return
        prev = self.head
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                prev.next = temp.next
                if temp == self.tail:
                    self.tail = prev
                return
            prev = temp
            temp = temp.next

    def search(self, key):
        if not self.head:
            print(f'CCL kosong. Tidak ada elemen yang bisa dicari.')
            return False
        temp = self.head
        if temp.data == key:
            print(f'Elemen {key} ditemukan dalam CCL.')
            return True
        temp = temp.next
        while temp != self.head:
            if temp.data == key:
                print(f'Elemen {key} ditemukan dalam CCL.')
                return True
            temp = temp.next
        print(f'Elemen {key} tidak ditemukan dalam CCL.')
        return False
    
    def merge(self, other):
        if not self.head:
            self.head = other.head
            self.tail = other.tail
            return        
        if not other.head:
            return
        self.tail.next = other.head
        temp = other.head
        while temp.next != other.head:
            temp = temp.next
        self.tail = temp
        self.tail.next = self.head

# LATIHAN 1
ll = CCL()
for e in [5, 10, 15, 20, 25, 30]:
    ll.insert(e)
print('CCL awal: ', end='')
ll.display()
ll.delete(5)
print('CCL setelah hapus 5: ', end='')
ll.display()

# LATIHAN 2
print('\nMencari 5:')
ll.search(5)
print('Mencari 15:')
ll.search(15)

# LATIHAN 4
print()
ll1 = CCL()
ll2 = CCL()
for e in [1, 3, 5, 7]:
    ll1.insert(e)
for e in [2, 4, 6, 8]:
    ll2.insert(e)
print('LL1: ', end='')
ll1.display()
print('LL2: ', end='')
ll2.display()
ll1.merge(ll2)
print('Setelah digabung: ', end='')
ll1.display()
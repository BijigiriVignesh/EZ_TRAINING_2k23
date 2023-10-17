class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class List:
    def __init__(self):
        self.head = None
    def insatend(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(value)
    def insatbegin(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node
    def delatbeg(self):
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next 
    def delatend(self):
        if not self.head.next:
            self.head = None
        else:
            temp = self.head
            while(temp.next.next):
                temp = temp.next
            temp.next = None
    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next
    def reverse(self):
        temp = self.head
        temp2 =None
        while(temp):
            tempo=temp.next
            temp.next =temp2
            temp2 = temp
            temp = tempo
        self.head =temp2
l = List()
l.insatend(15)
l.insatend(2)
l.insatend(12)

l.traverse()
l.reverse()
l.traverse()

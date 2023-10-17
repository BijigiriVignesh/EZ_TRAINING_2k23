class Node:
    def __init__(self,value):
        self.prev = None
        self.val = value
        self.next = None
class List:
    def __init__(self):
        self.head = None
    def insatbeg(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = Node(val)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    def travese(self):
        temp = self.head
        while(temp):
            print(temp.val,end = "->")
            temp = temp.next
    def insatend(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            tempo = Node(val)
            temp.next = tempo
            tempo.prev = temp
    def delatbeg(self):
        self.head = self.head.next
        self.head.prev =None
    def delatend(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next =None
    def reverse(self):
        temp = self.head
        while(temp):
            temp.next ,temp.prev = temp.prev,temp.next
            self.head=temp
            temp = temp.prev
lis = List()
lis.insatbeg(1)
lis.insatbeg(2)
lis.insatbeg(3)
lis.insatbeg(4)
print("insatbeg\n")
lis.travese()
lis.insatend(5)
lis.insatend(6)
lis.insatend(7)
print("\ninsatend\n")
lis.travese()
print("delatbeg")
lis.delatbeg()
lis.travese()
print("delatend")
lis.delatend()
lis.travese()
lis.reverse()
print("\nreverse")
lis.travese()
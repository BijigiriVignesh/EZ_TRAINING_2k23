class node:
    def __init__(self,value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,val):
        temp = node(val)
        temp.next = self.head
        self.head = temp
    def insert_at_end(self,val):
        if (self.head is None):
            self.head = node()
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = node(val)
    def traversal(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end = "->")
            temp = temp.next
linkedlist = LinkedList()
for i in range(5):
    linkedlist.insert_at_begin(i)
linkedlist.traversal()


        



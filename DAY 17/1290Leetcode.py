# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        temp = head
        c = 0
        while(temp):
            temp = temp.next
            c +=1
        temp = head
        while(temp):
            decimal += pow(2,c-1)*temp.val
            c-=1
            temp =temp.next
            print(decimal)
        return decimal
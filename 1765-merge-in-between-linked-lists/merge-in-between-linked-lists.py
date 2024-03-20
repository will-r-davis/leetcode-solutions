# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # storing references to list1's insertion points
        head1 = nodeBeforeA = list1
        head2 = list2
        while list2.next != None:
            list2 = list2.next
        
        while b >= -1:
            if a == 1:
                nodeBeforeA = list1
            if b == -1:
                list2.next = list1
            list1 = list1.next
            a -= 1
            b -= 1
        nodeBeforeA.next = head2
        return head1



        
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

    
    """
    Traversing linked lists typically leads to reference vs. copy issues.
    Avoiding such issues while maintaining efficiency can lead to code that is somewhat difficult to read.
    I wanted to pin the following code (not my own) which solves the problem while maintaining clarity 
    and readability by creating two well-named subfunctions.
    """

# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         def getTail(tail):
#             while tail and tail.next:
#                 tail = tail.next
#             return tail

#         def getNodesAtIndex(head, k1, k2):
#             first = second = head
#             for i in range(k2):
#                 if i == k1: first = second
#                 second = second.next
#             return first, second
        
#         node1, node2 = getNodesAtIndex(list1, a - 1, b)
#         list2Tail = getTail(list2)
#         node1.next, list2Tail.next = list2, node2.next

#         return list1
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        first, second = dummy, head
        # i = 0
        # maintain n distance between first and second
        while n > 0 and second:
            second = second.next
            n -= 1

        # while mainting the distance move forward while second reaches none
        while second:
            first = first.next
            second = second.next

        # break the link
        first.next = first.next.next

        return dummy.next


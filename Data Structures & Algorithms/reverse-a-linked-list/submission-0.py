# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        cur = head
        while cur != None:
            tmp = cur.next
            cur.next = left
            left = cur
            cur = tmp

        return left
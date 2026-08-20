# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        head = final
        left = list1
        right = list2
        while left and right:
            if left.val <= right.val:
                final.next = left
                left = left.next
            else:
                final.next = right
                right = right.next
            final = final.next 

        if left:
            final.next = left
        else:
            final.next = right

        return head.next
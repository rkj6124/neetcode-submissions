# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # second half
        second = slow.next

        # break the list in two halves, by making first half last node point to None
        slow.next = None

        # reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # after above loop prev would be at the head of reverse list
        # we will need 2 pointes pointing at the start of each half now
        first, second = head, prev

        # using slow and fast pointers,  the second list would be either 
        # equal or less than the first half, 
        # so we can iterate till we exhause the second list
        while second:
            # need to update next but to advance each pointers to next position
            # we will need temp vars
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next # get the link for the next node
            curr.next = prev # assign the current node link to the previous node

            prev = curr # move previous node to one ahead
            curr = temp # move current node to one ahead
        
        return prev
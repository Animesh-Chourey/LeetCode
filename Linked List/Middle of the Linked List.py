# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next # Move the fast pointer two spaces ahead
            slow = slow.next # Move the slow pointer one space only
        
        return slow

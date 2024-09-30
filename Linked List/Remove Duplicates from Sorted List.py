# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        # while the current node exists and the next node exists
        while curr and curr.next:
            if curr.val == curr.next.val: # current nodes value is equal to the next nodes value
                curr.next = curr.next.next # shift the pointer to the next to the next node
            else:
                curr = curr.next
        
        return head
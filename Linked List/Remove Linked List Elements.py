# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0)
        dummy.next = head # point it towards the head

        curr = head
        prev = dummy
        
        while curr:
            if curr.val == val:
                prev.next = curr.next # if the node's value matches the value to be checked, move the pointer to next
                curr = curr.next # move the current node as well
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next # always the head will be dummy.next
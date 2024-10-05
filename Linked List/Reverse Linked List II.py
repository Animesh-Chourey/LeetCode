# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr1 = head
        curr2 = head
        # final = head
        counter1 = 0
        counter2 = 0

        while curr1:
            counter1 += 1
            if counter1 >= left and counter1 <= right:
                temp = curr1.next
                curr1.next = prev

                prev = curr1
                curr1 = temp
            else:
                curr1 = curr1.next
        
        final = curr2
        while curr2:
            counter2 += 1
            if counter2 >= left and counter2 <= right:
                curr2.val = prev.val
                prev = prev.next
            else:
                curr2 = curr2.next
        
        return head
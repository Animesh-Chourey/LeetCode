class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # The intention is to find the mid point
        # Reverse the linked list after that
        # Compare the first half and the second half
        
        prev = None
        fast = head
        slow = head

        # Get the middle point the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the linked list
        while slow:
            temp = slow.next
            slow.next = prev

            prev = slow
            slow = temp

        
        left = head
        right = prev

        # Iterate until the value mismatches
        while right:
            if left.val != right.val:
                return False
    
            left = left.next
            right = right.next
        return True
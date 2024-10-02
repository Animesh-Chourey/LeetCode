# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {} # create a dict
        flag = 1
        curr = head

        while curr and curr.next:
            if curr.next not in visited: #store the pointers as key in dictionary 
            # so if we get the node having similar pointer value we can detect it
                visited[curr.next] = 0
                curr = curr.next
            else:
                return True
        
        if flag == 1:
            return False
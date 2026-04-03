# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers at the head of the list
        slow = head
        fast = head
        
        # Traverse the list. We check `fast` and `fast.next` to 
        # ensure we don't hit a NoneType error when taking two steps.
        while fast and fast.next:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next     # Move fast pointer two steps
            
            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True
                
        # If the fast pointer reaches the end of the list (None), 
        # there is no cycle.
        return False
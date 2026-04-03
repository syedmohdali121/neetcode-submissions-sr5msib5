# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head.
        # This handles edge cases, like removing the very first node in the list.
        dummy = ListNode(0, head)
        
        # Initialize two pointers, both starting at the dummy node
        left = dummy
        right = head
        
        # 1. Move the 'right' pointer forward by 'n' steps to create the gap
        for _ in range(n):
            right = right.next
            
        # 2. Move both pointers forward at the same speed until 'right' reaches the end
        while right:
            left = left.next
            right = right.next
            
        # 3. 'left' is now positioned exactly one node BEFORE the node we want to remove.
        # Skip the target node by updating the pointer.
        left.next = left.next.next
        
        # Return the new head of the list
        return dummy.next
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
            next_node = curr.next  # 1. Temporarily store the next node
            curr.next = prev       # 2. Reverse the pointer of the current node
            prev = curr            # 3. Move the 'prev' pointer one step forward
            curr = next_node       # 4. Move the 'curr' pointer one step forward
            
        # At the end, 'curr' is None, and 'prev' is pointing to the new head
        return prev     
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #handele edge case: empty list
        if head is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            #if both pointers meet, cycle exists
            if slow == fast:
                return True
            
        
        #if fast reached end, no cycle
    
        return False
        
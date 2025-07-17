# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """ 
        N = # of elements in the linked list

        Spacetime Complexity: O(1) time 
        - No additional data structures were created or used 

        Runtime Complexity: O(N)
        - worst case: we go through the whole linked list 
        """ 

        # check the base cases 
        if head.next == None or head == None: 
            return False  
        
        slow_ptr = head 
        fast_ptr = head.next 
    
        while fast_ptr != slow_ptr:
            if fast_ptr == None or fast_ptr.next == None:
                return False 

            slow_ptr = slow_ptr.next 
            fast_ptr = fast_ptr.next.next 
        
        return True 
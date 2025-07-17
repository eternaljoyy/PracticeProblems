# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        Runtime Complexity: O(N) 
         - Tarversing linearly over the Linked List 

        Spacetime Complexity: O(1)
         - Constant since not making any new data structures    
        """
        
        if head == []:
            return [] 
        elif head == None:
            return None 
        elif head.next == None:
            return head.val 
        else: 
            # adjust links to reverse the linked list 
            prev = None
            curr = head 

            while (head != None):
                curr = head.next 
                head.next = prev 
                prev = head 
                head = curr 
            return prev 
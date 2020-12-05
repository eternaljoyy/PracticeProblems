# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rangeSumBST(root, low, high):
	count = 0

	#Base case: root == None 
	if(root == None):
		return 
	
	if(low <= root.val <= high):
		count += root.val 

	rangeSumBST(root.left, low, high)
	rangeSumBST(root.right, low, high)	  
	return count 

rangeSumBST([10,5,15,3,7, None,18], 7, 15)	   
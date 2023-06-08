def PostorderTraversal(root): 

    if not root:
        return None 
    
    PostorderTraversal(root.left)
    PostorderTraversal(root.right)
    print(root.value)
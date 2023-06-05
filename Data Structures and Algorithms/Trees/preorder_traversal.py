def preorder_traversal(root):  
    if not root:
        return None 

    print(root)
    preorder_traversal(root.left)
    preorder_traversal(root.right)
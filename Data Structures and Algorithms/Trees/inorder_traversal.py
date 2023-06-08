def InorderTraversal(node): 
    
    InorderTraversal(node.left)
    print(node.value)
    InorderTraversal(node.right)
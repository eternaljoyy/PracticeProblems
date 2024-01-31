class BinarySearchTree:

    def __init__(self, val): 
        this.val = val 
        this.leftChild = None
        this.rightChild = None


    def insert(value, node): 
        if value > this.node:
            insert(value, this.rightChild)
        elif value < this.node:
            insert(value, this.leftChild) 
        else: 
            newNode = BinarySearchTree(value)

    
    def remove(BinarySearchTree root, key): 
        '''
        - Remove given key from the BST  
        ''' 
    
        if search(key) != True: 
            print('Node not present in the tree - cannot be deleted')
            return None

        if key < root.val: 
            root.left = remove(root.left, key) 
        elif key > root.val:
            root.right = remove(root.right, key) 
        else:  

            #TODO ~ Reached a leaf node 
            if isLeaf(root):
                 
            elif root.left == None: 
                temp = root.right
                root.val = temp.val
                root.right = None 
            elif root.right == None:
                temp = root.left 
                root.val = temp.val 
                root.left = None 
            else: 
                # Find the minimum val in the right sub-tree
                minNode = minValNode(root.right)
                root.val = minNode.val 

                # Remove the child that was copied 
                root.right = remove(root.right, minNode.val)
                

    def search(value, root):  

        if root.value == value:
            return True
        elif value > root:
            search(value, root.right)
        else:
            search(value, root.left)  

    
    # Check if the root node is a leaf node
    def isLeaf(root):
        if root.left and root.right == None:
            return True 
        return False 


    # Find the minimum node of sub-tree 
    def minValNode(root):

        while root.left != None:
            root = root.left 
        return root 
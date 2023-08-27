class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

#This function is used to find the minimum value 
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

#This function does the removing
def remove(root, val):
    if not root:
        return None
    
#makes the child null by removing it
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)

#Base case where the node you want to remove is the first one
    else:

        #checks to see if either child is null and return the one that isn't null
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        

        else:
            #find the value of the minimum node of the right subtree and store it in a value
            minNode = minValueNode(root.right)

            #assign its value as the root.val
            root.val = minNode.val

            #remove the old one 
            root.right = remove(root.right, minNode.val)

    return root


#Time complexity is O
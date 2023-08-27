class TreeNode:
    def __init__(self, val, left=None, right=None):
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

#function to visualize by level
def print_tree_by_levels(root):
    if not root:
        return
    
    queue = [root]
    
    while queue:
        level_values = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print(level_values)

mytree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))

remove(mytree, 4)
print_tree_by_levels(mytree)
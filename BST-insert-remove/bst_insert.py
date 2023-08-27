class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def insert (root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

mytree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))



"""   Tree:

             A4
           /    \
         B2     C6
        /  \   /  \
        D1 E3 F5  G7
"""

#we check if the passed in value is greater or less than the value of the root node

#if it is greater, we make it right node
#if it is less, we make it the left node

#if it is the base case aka there is nothing next, we insert the node

#If a balanced tree, time complexity is O(logn)
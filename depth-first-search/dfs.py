#depth first search time complexity is O(V + N) where V is the number of vertices(nodes), and E is the number of edges

#adding insertion to the search tree adds O(logn) to the time complexity

#building the entire tree would be O(logn)

#In each function, the print statement is where you'd wanna replace to append or pop that value to an array for example.

#Tree:

        #     A4
        #   /    \
        # B2     C6
        #/  \   /  \
        #D1 E3 F5  G7

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#preorder explores the left side of the tree then the right side
def dfs_preorder(root):
    if not root:
        return
    print(root.val)
    dfs_preorder(root.left)
    dfs_preorder(root.right)


#Goes in ascending order according to their values". The left subtree contains smaller values (usually) and the right side contains larger values
def dfs_inorder(root):
    if not root:
        return
    dfs_inorder(root.left)
    print(root.val)
    dfs_inorder(root.right)


#postorder explores the right side then the left side
def dfs_postorder(root):
    if not root:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val)
    

#Explores in reverse order from largest value to smallest value
def dfs_reverse(root):
    if not root:
        return
    dfs_reverse(root.right)
    print(root.val)
    dfs_reverse(root.left)


mytree = Node('A4', Node('B2', Node('D1'), Node('E3')), Node('C6', Node('F5'), Node('G7')))

dfs_inorder(mytree)



#If you need to add the nodes to a list in a certain order, add an empty list and replace the print statements with list_name.append(root.val). Then return whatever spot of the list value you need

#Example: Leetcode 230

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res[k-1]
    
#But a more efficient way is this solution where you stop early:
def kthSmallest_dfs_early_stopping(self, root, k):
	res = []
	def _inorder(node):
		if not node: return
		_inorder(node.left)
		if len(res) == k:
			return
		res.append(node.val)
		_inorder(node.right)
	_inorder(root)
	return res[-1]


#Iterative solution

def inorderTraversal(self, root):
    res = []
    stack = []

    #set up a current pointer to point to the root
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

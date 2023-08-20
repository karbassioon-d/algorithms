"""   Tree:

             A4
           /    \
         B2     C6
        /  \   /  \
        D1 E3 F5  G7
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def bfs(root):

    queue = deque()
    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("Level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
        
mytree = Node('A4', Node('B2', Node('D1'), Node('E3')), Node('C6', Node('F5'), Node('G7')))

bfs(mytree)
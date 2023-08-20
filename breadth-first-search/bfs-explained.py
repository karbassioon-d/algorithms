#Isn't a recursion algorithm
#Is also known as level order traversal

#Uses a queue data structure to process nodes (first in first out)

#Time complexity is O(c * n) which reduces to O(n)

#probably one of the most common algorithms you'll use

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
#deque is a Doubly Ended Queue. It's preffered over a list in the cases where we need quicker append and pop operations from both ends of the container. It provies a O(1) time complexity for append and pop operations where list pop and append operations are O(n).

def bfs(root):

    queue = deque()

    #check to see if there is a root node, and if there is, append the node to the queue
    if root:
        queue.append(root)
        
    #use level to see how deep we are in the tree/graph
    level = 0

    #as long as we have a node in the queue, we'll continue the operations
    while len(queue) > 0:

        print("Level: ", level)

        #keep going for the length of the queue. It'll stop when the queue is empty meaning we've visited all the nodes
        for i in range(len(queue)):

            #popleft is a method of the dequeue class and removes an element from the left side of the deque and returns the value. Since bfs uses a FIFO structure we use popleft
            curr = queue.popleft()
            print(curr.val)

            #check to see if there's a left/right value, and if there is, add it to the deque
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        #incrememnt the level counter to update its value
        level += 1
        
mytree = Node('A4', Node('B2', Node('D1'), Node('E3')), Node('C6', Node('F5'), Node('G7')))

bfs(mytree)
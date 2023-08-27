class TreeNode {
    constructor(val, left=null, right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function minValueNode(root) {
    let curr = root;
    while (curr && curr.left) {
        curr = curr.left;
    }
    return curr;
}

function remove(root, val) {
    if (!root) {
        return null
    }

    if (val > root.val) {
        root.right = remove(root.right, val)
    } else if (val < root.val) {
        root.left = remove(root.left, val)
    } else {
        if (!root.left) {
            return root.right;
        } else if (!root.right) {
            return root.left;
        } else {
            let minNode = minValueNode(root.right);
            root.val = minNode.val;
            root.right = remove(root.right, minNode.val);
        }
    }
    return root;
}

const myTree = new TreeNode(4,
    new TreeNode(2,
        new TreeNode(1),
        new TreeNode(3)
    ),
    new TreeNode(6,
        new TreeNode(5),
        new TreeNode(7)
    )
);

function printTreeByLevels(root) {
    if (!root) {
        return;
    }
    
    const queue = [root];
    
    while (queue.length > 0) {
        const levelValues = [];
        const levelSize = queue.length;
        
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            levelValues.push(node.val);
            
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
        
        console.log(levelValues);
    }
}

remove(myTree, 4);
printTreeByLevels(myTree);
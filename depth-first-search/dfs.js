class Node {
    constructor(val, left=null, right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/*    Tree:

             A4
           /    \
         B2     C6
        /  \   /  \
        D1 E3 F5  G7
*/

//Explores the left side of the tree, then the right side
function dfsPreorder(root) {
    if (!root) {
        return
    };
    console.log(root.val);
    dfsPreorder(root.left);
    dfsPreorder(root.right);
}

//Goes in ascending order according to their values
function dfsInorder(root) {
    if (!root) {
        return
    };
    dfsInorder(root.left);
    console.log(root.val);
    dfsInorder(root.right);
}

//Explores the right side of the tree then the left
function dfsPostorder(root) {
    if (!root) {
        return
    };
    dfsPostorder(root.left);
    dfsPostorder(root.right);
    console.log(root.val);
}

//Explores in reverse order from largest value to smallest value
function dfsReverse(root) {
    if (!root) {
        return
    };
    dfsReverse(root.right);
    console.log(root.val);
    dfsReverse(root.left);
}

const myTree = new Node('A4',
    new Node('B2',
        new Node('D1'),
        new Node('E3')
    ),
    new Node('C6',
        new Node('F5'),
        new Node('G7')
    )
);
dfsPreorder(myTree);
class Node {
    constructor(val, left=null, right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function dfsPreorder(root) {
    if (!root) {
        return;
    }
    console.log(root.val);
    dfsPreorder(root.left);
    dfsPreorder(root.right);
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
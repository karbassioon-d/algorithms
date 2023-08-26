/*   Tree:

             A4
           /    \
         B2     C6
        /  \   /  \
        D1 E3 F5  G7
*/

class TreeNode {
    constructor(val, left=null, right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function bstInsert(root, val) {

    if (!root) {
        return new TreeNode(val);
    }

    if (val > root.val) {
        root.right = bstInsert(root.right, val);
    } else if (val < root.val) {
        root.left = bstInsert(root.left, val);
    }
    console.log(root);
    return root

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

bstInsert(myTree, 9);

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

function bfs(root) {
    
    const queue = [];
    if (root) {
        queue.push(root);
    }

    let level = 0;
    while (queue.length > 0) {
        console.log("Level: ", level);
        const levelSize = queue.length; //needed
        for (let i = 0; i < levelSize; i++) {
            const curr = queue.shift();
            console.log(curr.val);
            if (curr.left) {
                queue.push(curr.left)
            }
            if (curr.right) {
                queue.push(curr.right);
            }
        }
        level++;
    }
};


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

bfs(myTree);
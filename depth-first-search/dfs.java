class Node {
    int val;
    Node left;
    Node right;

    public Node(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class dfs {

    public static void dfsPreorder(Node root) {
        if (root == null) {
            return;
        }
        System.out.println(root.val);
        dfsPreorder(root.left);
        dfsPreorder(root.right);
    }
    
    public static void main(String[] args) {
        // Create the binary tree
        Node tree = new Node(1);
        tree.left = new Node(2);
        tree.right = new Node(3);
        tree.left.left = new Node(4);
        tree.left.right = new Node(5);
        tree.right.left = new Node(6);
        tree.right.right = new Node(7);

        // Perform DFS preorder traversal
        dfsPreorder(tree);
    }
}
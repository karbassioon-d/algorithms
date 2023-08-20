import java.util.LinkedList;
import java.util.Queue;

class Node {
    int val;
    Node left, right;

    public Node(int val) {
        this.val = val;
        left = right = null;
    }
}

public class bfs {

    public static void breadthFirstSearch(Node root) {
        Queue<Node> queue = new LinkedList<>();
        if (root != null) {
            queue.add(root);
        }

        int level = 0;
        while(!queue.isEmpty()) {
            System.out.println("Level: " + level);
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                Node curr = queue.poll();
                System.out.println(curr.val);
                if (curr.left != null) {
                    queue.add(curr.left);
                }
                if (curr.right != null) {
                    queue.add(curr.right);
                }
            }
            level++;
        }
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

        breadthFirstSearch(tree);
    }
}

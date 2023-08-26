using System;
using System.Collections.Generic;

class TreeNode {
    public int val;
    public TreeNode? left;
    public TreeNode? right;

    public TreeNode(int val, TreeNode? left = null, TreeNode? right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public override string ToString()
    {
        return $"Node({val})";
    }
}

class Program
{
    static TreeNode BstInsert(TreeNode? root, int val)
    {
        if (root == null)
        {
            return new TreeNode(val);
        }

        if (val > root.val)
        {
            root.right = BstInsert(root.right, val);
        } else if (val < root.val)
        {
            root.left = BstInsert(root.left, val);
        }

        return root;
    }

    //Here, we make a new method that takes in a TreeNode and a list of values that are ints where the values of the nodes are collected
    static void CollectTreeValues(TreeNode? node, List<int> values)
    {
        if (node == null) return;
        CollectTreeValues(node.left, values);
        values.Add(node.val);
        CollectTreeValues(node.right, values);
    }

    static void Main(string[] args) {
    TreeNode? myTree = new TreeNode(4,
        new TreeNode(2,
            new TreeNode(1),
            new TreeNode(3)
        ),
        new TreeNode(6,
            new TreeNode(5),
            new TreeNode(7)
        )
    );

    myTree = BstInsert(myTree, 9);
    
    //creating a new List<int> which will be used to store the values of the nodes in the BT
    List<int> treeValues = new List<int>();
    CollectTreeValues(myTree, treeValues);

    foreach (int value in treeValues)
    {
        Console.Write(value + " ");
    }
   }
}
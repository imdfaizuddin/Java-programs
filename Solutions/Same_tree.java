/*
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
*/
/*
class TreeNode {
    int data;
    TreeNode left;
    TreeNode right;

    public TreeNode() {}
    public TreeNode(int data) {
        this.data = data;
    }

    public TreeNode(int data, TreeNode left, TreeNode right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}
*/

class Solution {
    boolean help(TreeNode p, TreeNode q){
        if(p == null && q == null) return true;
        if(p == null) return false;
        if(q == null) return false;
        if(p.val != q.val)return false;
            if( help(p.left ,q.left) ==true && help(p.right, q.right)== true ){
            return true;
            }else{
                return false;
            }
            
    }
	public boolean isSameTree(TreeNode p, TreeNode q) {
		// Your code goes here
        return help(p,q);
	}
}

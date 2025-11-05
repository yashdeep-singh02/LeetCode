/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null)
        {
            return false;
        }

        int newtarget = targetSum-root.val;

        if((root.left==null)&&(root.right==null))
                return newtarget==0;

        boolean leftPath = hasPathSum(root.left,newtarget);
        boolean rightPath = hasPathSum(root.right,newtarget);

        return (leftPath||rightPath);
        
    }
}
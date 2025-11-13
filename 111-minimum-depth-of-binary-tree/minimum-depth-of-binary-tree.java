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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;

        }

        int ldepth = minDepth(root.left);
        int rdepth = minDepth(root.right);
        if(ldepth==0 || rdepth==0)
            return Math.max(ldepth,rdepth)+1;
        return Math.min(ldepth, rdepth) + 1;
    }
}

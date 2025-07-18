# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def invertTree(self, node, firstCall=True, root=None):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        
        Input - Binary Tree
        Output - Inverted Binary Tree (make all left children right children, vice versa)
        Basically instead of the smaller elements being on the LHS and biggeer on the RHS
        Now its the other way around
        Approach - Recursion
        """
        if firstCall:
            root = node
            firstCall = False
            
        # Base case - nothing to invert
        if node.left is None and node.right is None:
            return root
        
        

# https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg
tree = TreeNode(4,TreeNode(2),TreeNode(7))
tree.left.left = TreeNode(1)
tree.right.right = TreeNode(9)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
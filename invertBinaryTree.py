# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def exploreTree(self, node):
        if node is None:
            print()
        if node.left:
            print(f"Left child of {node.val}: {node.left.val}")
            self.exploreTree(node.left)
        if node.right:
            print(f"Right child of {node.val}: {node.right.val}")
            self.exploreTree(node.right)

    def invertTree(self, node):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        
        Input - Binary Tree
        Output - Inverted Binary Tree (make all left children right children, vice versa)
        Basically instead of the smaller elements being on the LHS and biggeer on the RHS
        Now its the other way around
        Approach - Recursion, DFS style, swap the left and right's (from top to bottom, left to right)
        Base case - no swap to complete, node arg is none
        Recursive case - the current node has downstream children whose children etc. need to be swapped
        """
        root = None
        firstCall = True
        if firstCall:
            root = node
            firstCall = False

        res = self.auxInvertTree(root)
        return root
        
        
    def auxInvertTree(self, node):
        if node is None:
            return
        
        oldLeft = node.left
        node.left = node.right
        node.right = oldLeft

        self.invertTree(node.left)
        self.invertTree(node.right)
        return
        


        
        

# https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg
rootNode = TreeNode(4,TreeNode(2),TreeNode(7))
rootNode.left.left = TreeNode(1)
rootNode.right.right = TreeNode(9)
rootNode.left.right = TreeNode(3)
rootNode.right.left = TreeNode(6)

sol = Solution()
res = sol.invertTree(rootNode)
print(res.val, res.left.val, res.right.val)
sol.exploreTree(res)
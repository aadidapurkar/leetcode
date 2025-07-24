from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recurseLeft(self, node, depth = 0):
        if node is None or node.left is None:
            return depth
        else:
            depth += 1
            return self.recurseLeft(node.left, depth)

    def recurseRight(self, node, depth = 0):
        if node is None or node.right is None:
            return depth
        else:
            depth += 1
            return self.recurseRight(node.right, depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        For any node, the height difference between the left and right subtree must be 1 or 0
        Must check all nodes

        Every time we discover a new node object, we could append it to a set
        """
        left = self.recurseLeft(root)
        right = self.recurseRight(root)
        heightDiff = abs(right - left)
        if heightDiff not in [0,1]:
            return False
        else:
            if root:
                if root.left:
                    self.isBalanced(root.left)
                if root.right:
                    self.isBalanced(root.right)
        return True
    

sol = Solution()
root = TreeNode(3, TreeNode(9),TreeNode(20))
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.isBalanced(root))
root2 = TreeNode(1,TreeNode(2), TreeNode(2))
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)
print(sol.isBalanced(root2))
# [1,2,3,4,5,6,null,8]
root3 = TreeNode(1, TreeNode(2), TreeNode(3))
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
root3.right.left = TreeNode(6)
root3.right.left.left = TreeNode(8)
print(sol.isBalanced(root3))
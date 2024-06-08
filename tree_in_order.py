# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class Solution(object):
    def kthSmallest(self, root, k):
        values = []
        self.inorder(root, values)
        return values[k - 1]

    def inorder(self, root, values):
        if root is None:
            return
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    solution = Solution()
    # Test case 1: k = 1
    assert solution.kthSmallest(root, 1) ==  2

    # Test case 2: k = 3
    assert solution.kthSmallest(root, 3) ==  4

    # Test case 3: k = 6
    assert solution.kthSmallest(root, 6) == 7
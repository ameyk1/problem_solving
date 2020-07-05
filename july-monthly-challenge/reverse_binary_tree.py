# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def invertTree(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def inorder_traversal(root):
    if not(root):
        return
    inorder_traversal(root.left)
    print(root.val, end = " ")
    inorder_traversal(root.right)

def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print ("Binary Tree")
    inorder_traversal(root)
    print("\n")
    sol = Solution()
    reverse_root = sol.invertTree(root)
    inorder_traversal(reverse_root)

if __name__ == '__main__':
    main()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        new_root = TreeNode(root.val)
        queue = deque([(root, new_root)])

        while queue:
            node, new_node = queue.popleft()

            if node.left:
                new_node.right = TreeNode(node.left.val)
                queue.append((node.left, new_node.right))

            if node.right:
                new_node.left = TreeNode(node.right.val)
                queue.append((node.right, new_node.left))

        return new_root
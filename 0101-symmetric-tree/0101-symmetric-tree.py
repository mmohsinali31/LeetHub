# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        queue1=deque([root.left])
        queue2=deque([root.right])
        while queue1 and queue2:
            node1=queue1.popleft()
            node2=queue2.popleft()
            if node1 is None and node2 is None:
               continue
            if node1 is None or node2 is None:
               return False

            if node1.val != node2.val:
               return False
            if node1.left or node2.right:
                queue1.append(node1.left)
                queue2.append(node2.right)
            if node1.right or node2.left:
                queue1.append(node1.right)
                queue2.append(node2.left)
        return True



        
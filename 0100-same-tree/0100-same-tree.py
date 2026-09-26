# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue1=deque([p])
        queue2=deque([q])
        while queue1 or queue2:
            for i in range(len(queue1)):
                node1=queue1.popleft()
                node2=queue2.popleft()
                if node1 is not None and node2 is not None :
                    if node1.val != node2.val :
                      return False
                if node1 is not None and node2 is  None or node1 is  None and node2 is not None:
                    return False
                if node1 is None and node2 is None:
                    continue
                if node1.left or node2.left:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                if node1.right or node2.right:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
        return True
        
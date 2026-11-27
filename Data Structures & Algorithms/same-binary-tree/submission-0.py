# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def dfs(p,q):
        #     left, right= dfs(p.left), dfs(p.right)
        #     left2, right2= dfs(q.left), dfs(q.right)
        #     if left==left2 and right==right2:
        #         return True
        # return dfs(p,q) wrong
        if not p and not q: return True
        
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        else:
            return False



    
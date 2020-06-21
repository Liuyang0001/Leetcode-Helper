#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] all-nodes-distance-k-in-binary-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # 如果节点有指向父节点的引用，也就知道了距离该节点 1 距离的所有节点。
        # 之后就可以从 target 节点开始进行深度优先搜索了。
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        # 对所有节点添加一个指向父节点的引用，之后做深度优先搜索，
        # 找到所有距离 target 节点 K 距离的节点。
        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue] # 找到所有距离 target 节点 K 距离的节点。
            node, d = queue.popleft() # dfs从头搜索
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:#only focus on the nodes not seen
                    seen.add(nei)
                    queue.append((nei, d+1)) # 把当前节点的parent, left,right（未搜过的）加入搜索

        return []
# @lc code=end
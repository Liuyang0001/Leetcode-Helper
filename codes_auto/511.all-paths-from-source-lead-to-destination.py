#
# @lc app=leetcode.cn id=511 lang=python
#
# [511] all-paths-from-source-lead-to-destination
#
class Solution(object):

    def dfs(self, cur, target, link, visited):
        if cur == target:
            return True
        # 没有出度，且不为终点
        if cur not in link:
            return False

        visited.add(cur)
        for next in link[cur]:
            # 有环
            if next in visited:
                # 取消这个计算过的路径的【标记】节约时间
                visited.remove(cur)
                return False
            # 下一个路径走不到
            if not self.dfs(next, target, link, visited):
                # 取消这个计算过的路径的【标记】节约时间
                visited.remove(cur)
                return False

        #【关键】记得取消这个计算过的路径的【标记】
        visited.remove(cur)
        return True

    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
         从起点开始dfs，与平常dfs不同的是，要用一个数组onPath记录当前有哪些点处于正在走的路径上。对于每一个遍历到的点，如果该点是一个没有出度的点，则直接返回当前点是否是终点，否则遍历其所有邻边，如果找到一个邻点在当前已经走过的路径上，说明该图有环，则不能到达终点，如果所有的邻边有一条检测到环或者走到不是终点的停止点则返回false，否则如果所有的边都能最后停在终点处则返回true。
        """
        link = {}
        for s, e in edges:
            if s not in link:
                link[s] = []
            link[s].append(e)

        # 终点不可能有出边
        if destination in link:
            return False

        return self.dfs(source, destination, link, set())

# @lc code=end
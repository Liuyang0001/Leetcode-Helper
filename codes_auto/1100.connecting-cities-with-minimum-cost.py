#
# @lc app=leetcode.cn id=1100 lang=python3
#
# [1100] connecting-cities-with-minimum-cost
#
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        '''
        \U0001f942Kruskal算法 = 并查集+贪心, 不断加入直至N-1条 不会构成环的最小权重边
        '''
        #并查集初始化
        p = [i for i in range(N + 1)]
        #按边的长度升序排序，贪心初始化      
        connections.sort(key = lambda x: x[2])     
        #查找修改所属集合
        def f(x):
            if p[x] != x:
                p[x] = f(p[x])
            return p[x]
        count = 0
        ans = 0
        for x, y, c in connections:
            px, py = f(x), f(y)
             #属于不同集合的时候，累加值里添加上边的长度，并且合并集合
            if px != py:       
                count += 1
                ans += c
                p[px] = py
                #添加了足够的点，就返回
                if count == N - 1:     
                    return ans
        return -1
# @lc code=end
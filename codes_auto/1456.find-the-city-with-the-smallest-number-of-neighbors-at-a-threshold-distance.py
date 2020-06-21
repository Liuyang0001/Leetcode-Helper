#
# @lc app=leetcode.cn id=1456 lang=python
#
# [1456] find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
#
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # 定义二维D向量，并初始化各个城市间距离为（无穷）
        map = [[10000 for i in range(n)] for j in range(n)]
        for i,j,weight in edges:
            map[i][j] = weight
            map[j][i] = weight
        # Floyd算法，注意K一定在最外层
        for k in range(n):
             for i in range(n):
                  for j in range(n):
                      if(i!=j and map[i][j] > map[i][k] + map[k][j]):
                          map[i][j] = map[i][k] + map[k][j]
                          map[j][i]= map[i][j]
        max_count = n+1
        res = -1
        #选择出能到达其它城市最少的城市ret
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if(map[i][j]<= distanceThreshold):
        #             count +=1
        #     if max_count >= count:
        #         max_count = count
        #         res = i
        # return res
        return min(range(n),key=lambda i:(sum([1 for j in range(n) if i!=j and map[i][j]<=distanceThreshold]),-i))
# @lc code=end
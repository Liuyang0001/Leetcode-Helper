#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] minimum-number-of-arrows-to-burst-balloons
#
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 特判
        if len(points) < 2: return len(points)
        # 按照区间的起始端点排序
        points.sort(key=lambda x:x[0])
        
        # 起始区间至少一枚激光炮发射
        res = 1
        # 最远距离：使用当前这枚激光炮能击穿飞碟的最远距离
        end = points[0][1]
        C = [end]
        
        for point in points:
            if point[0] > end:
                C.append(end)
                end = point[1]
                res += 1
            else:
                end = min(end, point[1])
        return res

# @lc code=end
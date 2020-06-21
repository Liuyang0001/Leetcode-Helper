#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] water-and-jug-problem
#
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        #关键：公约数必整除z
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
# @lc code=end
#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] number-of-islands
#
class Solution:
    

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        if row ==0: return 0
        col = len(grid[0])
        # use dfs to change the neighbors into 0
        def dfs(i, j):
            grid[i][j]= '0'
            for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if 0<=x<row and 0<=y<col and grid[x][y]=='1':
                    dfs(x,y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

# @lc code=end
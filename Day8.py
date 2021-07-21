# https://leetcode.com/problems/island-perimeter/


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        extraRows = [[0 for i in range(len(grid[0]))]]
        grid = extraRows + grid + extraRows
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if grid[i][j] == 1:
                    neighbourCount = 0
                    if grid[i-1][j] == 1:
                        neighbourCount += 1
                    if grid[i+1][j] == 1:
                        neighbourCount += 1
                    if grid[i][j-1] == 1:
                        neighbourCount += 1
                    if grid[i][j+1] == 1:
                        neighbourCount += 1
                    perimeter += 4 - neighbourCount
        return perimeter
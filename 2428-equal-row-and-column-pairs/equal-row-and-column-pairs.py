class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        columns = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid))]

        for row in grid:
            for col in columns:
                if row == col:
                    count += 1
        return count
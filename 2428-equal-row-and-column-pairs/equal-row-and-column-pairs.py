class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gridLen = len(grid)
        count = 0
        for i in range(gridLen):
            curRow = grid[i]
            for colIdx in range(gridLen):
                # col = [grid[x][colIdx] for x in range(gridLen)]

                match = 1
                for x in range(gridLen):
                    if grid[x][colIdx] != curRow[x]:
                        match = 0
                
                count += match

        return count




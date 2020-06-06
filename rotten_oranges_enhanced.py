from typing import List

FRESH = 1
ROTTEN = 2


class Solution:

    def getCount(self, grid):
        fresh_count = 0
        rotten_count = 0

        for row in grid:
            for col in row:
                if col == FRESH:
                    fresh_count += 1
                elif col == ROTTEN:
                    rotten_count += 1

        return fresh_count, rotten_count

    def orangesRotting(self, grid: List[List[int]]) -> int:

        minute = 0
        new_rotten_list = []

        # First round - Get all rotten oranges
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == ROTTEN:
                    new_rotten_list = self.getFreshOrangeNeighbours(i, j, grid)
                    print(new_rotten_list)

        # If there are no rotten oranges, no other can rot too. RETURN -1
        if len(new_rotten_list) == 0:
            return -1

        # Iterate through the rotten oranges and get indexes of all fresh oranges that are their neighbours
        # The fresh neighbours are going to be rotten
        while True:
            for i, row in enumerate(grid):
                for j, elem in enumerate(row):
                    if elem == ROTTEN:
                        new_rotten_list = self.getFreshOrangeNeighbours(i, j, grid)
                        print(new_rotten_list)

            if len(new_rotten_list) == 0:
                print("new rotten list is empty")
                break
            else:
                for (i, j) in new_rotten_list:
                    grid[i][j] = 2

            print(grid)
            minute += 1

            print(grid)

        fresh_count, rotten_count = self.getCount(grid)
        if fresh_count > 0:
            print("There is a fresh left over")
            return -1

        return minute

    def getFreshOrangeNeighbours(self, i, j, grid):
        return self.infect(grid, i + 1, j) + self.infect(grid, i, j + 1) + self.infect(grid, i - 1, j) + self.infect(grid, i, j - 1)

    def infect(self, grid, row_index, col_index):

        try:
            if grid[row_index][col_index] == 1:
                print(f'I want to infect {row_index} {col_index}')
                return [(row_index, col_index)]
            else:
                return []
        except IndexError:
            return []

sol = Solution()
case1= [[2,1,1],[1,1,0],[0,1,1]] # 4 is answer
case2 = [[1],[2],[2]]
res = sol.orangesRotting(case2)
print(f"Result {res} Expected: 4")
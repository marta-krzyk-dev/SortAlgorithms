from typing import List

FRESH = 1
ROTTEN = 2


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        minute, freshCount = 0, 0
        rotten_oranges = []

        # First round - Get all rotten oranges
        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == ROTTEN:
                    rotten_oranges += [(i, j)]
                elif orange == FRESH:
                    freshCount += 1

        # If there are no rotten oranges, no other can rot too. RETURN -1
        if len(rotten_oranges) == 0:
            return -1

        # Iterate through the rotten oranges and get indexes of all fresh oranges that are their neighbours
        # The fresh neighbours are going to be rotten
        while True:
            fresh_oranges = []
            for i, j in rotten_oranges:
                fresh_oranges += self.getFreshOrangeNeighbours(i, j, grid)
            print(f"I want to infect {fresh_oranges}")

            if len(fresh_oranges) == 0:
                print("No new fresh orange was rotten")
                break
            else:
                fresh_oranges = set(fresh_oranges)  # Remove duplicates
                for (i, j) in fresh_oranges:
                    grid[i][j] = ROTTEN
                freshCount -= len(fresh_oranges)

            minute += 1
            rotten_oranges = fresh_oranges
            print(f"After {minute} minutes there are {freshCount} fresh oranges")
            print(f"Grid: {grid}")

        # There is at least 1 fresh orange who is not neighbour with a rotten orange
        if freshCount > 0:
            print("There is a fresh orange left over")
            return -1

        return minute

    def getFreshOrangeNeighbours(self, i, j, grid):
        return self.getIndexIfFresh(grid, i + 1, j) + self.getIndexIfFresh(grid, i, j + 1) + self.getIndexIfFresh(grid,
                                                                                                                  i - 1,
                                                                                                                  j) + self.getIndexIfFresh(
            grid, i, j - 1)

    def getIndexIfFresh(self, grid, row_index, col_index):

        if row_index < 0 or col_index < 0:
            return []
        try:
            if grid[row_index][col_index] == 1:
                return [(row_index, col_index)]
            else:
                return []
        except IndexError:
            return []


sol = Solution()
cases = [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[1], [2], [2]], 1)
]

for data, answer in cases:
    print(f"Result {sol.orangesRotting(data)} Expected: {answer}")
    print()
    print()

"""
goal: return number of islands
1 is land
0 is water
island is count of isolated collections of land
edges of grid are considered water
rows, x
cols, y
"""

class Solution:
    

    def land_search(self,i,j):

        if i >= self.rows or i < 0:
            return
        if j >= self.cols or j < 0:
            return

        if self.visited[i][j]:
            return

        if self.grid[i][j] == "0":
            self.visited[i][j] = True
            return

        if self.grid[i][j] == "1":
            self.visited[i][j] = True
            self.land_search(i-1,j)
            self.land_search(i+1,j)
            self.land_search(i,j+1)
            self.land_search(i,j-1)
            return

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.land_count = 0

        # binary array
        self.visited = []
        for _ in range(self.rows):
            self.visited.append([False]*self.cols)

        for i in range(self.rows):
            for j in range(self.cols):

                if self.visited[i][j]:
                    continue

                # if water add to visited, and continue
                if self.grid[i][j] == "0":
                    self.visited[i][j] = True
                    continue

                # when land find connecting pieces and increment land count
                if self.grid[i][j] == "1":
                    self.land_count += 1
                    self.land_search(i, j)
        return self.land_count

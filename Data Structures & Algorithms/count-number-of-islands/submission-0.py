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
        print(f"searching for land around {i} {j}")
        if i >= self.rows or i < 0:
            print(f"invalid at {i} {j}")
            return
        if j >= self.cols or j < 0:
            print(f"invalid at {i} {j}")
            return

        if self.visited[i][j]:
            print(f"search already visited at {i} {j}")
            return

        if self.grid[i][j] == "0":
            print(f"search found water at {i} {j}")
            self.visited[i][j] = True
            return

        if self.grid[i][j] == "1":
            print(f"adding {i} {j} to visited")
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
                    print(f"visited {i} {j}")
                    continue

                # if water add to visited, and continue
                if self.grid[i][j] == "0":
                    self.visited[i][j] = True
                    continue

                # when land find connecting pieces and increment land count
                if self.grid[i][j] == "1":
                    print(f"found land at {i} {j}")
                    self.land_count += 1
                    self.land_search(i, j)
                    print(self.visited)

        return self.land_count

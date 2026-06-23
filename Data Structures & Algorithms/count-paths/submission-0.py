class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m
        n = n
        # build cache backwards, then return number of paths starting at 0,0
        cache = {}

        def grid_search(x,y,m,n) -> int:

            if x > m or y > n:
                return 0

            if x < 0 or y < 0:
                return 0

            key = f"{x}_{y}"
            if key in cache.keys():
                return cache[key]
            
            if x==(m-1) and y==(n-1):
                return 1

            # can only move down and to the right
            paths = grid_search(x+1,y,m,n) + grid_search(x,y+1,m,n)
            cache[key] = paths

            return paths
        
        for x in range(m):
            for y in range(n):
                grid_search(m-x,n-y,m,n)
        
        return grid_search(0,0,m,n)
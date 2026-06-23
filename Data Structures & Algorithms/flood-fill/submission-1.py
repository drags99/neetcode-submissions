class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = {}
        m = len(image)
        n = len(image[0])
        starting_color = image[sr][sc]
        fill_color = color
        # print(f"fill_color color {fill_color}")

        def dfs_fill(image, sr, sc, m,n,fill_color,starting_color,visited):
            # print(f"fill_color color {fill_color}")
            
            visit_key = f"{sr}_{sc}"
            # print(visit_key)
            
            if visit_key in visited.keys():
                return image

            if (sr >= m) or (sr < 0):
                return image
            
            if (sc >= n) or (sc < 0):
                return image

            if image[sr][sc] == starting_color:
                # print(f"{visit_key}")
                # print(f"{visited}")
                image[sr][sc] = fill_color
            else:
                visited[visit_key] = 1
                return image

            visited[visit_key] = 1

            # check adjacent pixels
            dfs_fill(image, sr+1, sc, m,n,fill_color,starting_color,visited)     
            dfs_fill(image, sr-1, sc, m,n,fill_color,starting_color,visited)
            dfs_fill(image, sr, sc-1, m,n,fill_color,starting_color,visited)
            dfs_fill(image, sr, sc+1, m,n,fill_color,starting_color,visited)

            visited.pop(visit_key, None)

            return image
        
        return dfs_fill(image, sr, sc, m,n,fill_color,starting_color,visited)
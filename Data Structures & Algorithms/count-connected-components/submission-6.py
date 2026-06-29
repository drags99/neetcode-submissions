class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if two edge points to two nodes not seen, then is a new component
        counter = 0
        visited = set()
        
        def search(node: int):
            for e in edges:
                if (e[0] in visited) and (e[1] in visited):
                    continue

                if node == e[0]:
                    visited.add(e[1])
                    search(e[1])
                    continue

                if node == e[1]:
                    visited.add(e[0])
                    search(e[0])
                    continue
            return
        
        for e in edges:
            if e[0] not in visited:
                if e[1] not in visited:
                    counter += 1
                    visited.add(e[0])
                    search(e[0])


        
        return counter + (n-len(visited))
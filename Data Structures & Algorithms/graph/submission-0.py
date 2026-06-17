class Graph:
    
    def __init__(self):
        # each node containes the id as the key and returns nodes it is connected to
        self.nodes = {}

    def _init_node(self,node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = []

    def addEdge(self, src: int, dst: int) -> None:
        # check if src and dst are in the nodes and add them if not
        # init the src and dst if they arent in the nodes hashmap
        self._init_node(src)
        self._init_node(dst)

        self.nodes[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # check if edge from src to dst exists
        if src in self.nodes:
            # check if a edge exists from src to dst
            if dst in self.nodes[src]:
                # remove the edge
                self.nodes[src].remove(dst)
                return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        # run dfs  from src to see if we find dst
        queue = []
        visited = set()
        queue.append(src)
        # while queue is not empty
        while queue:

            # pop first item in list
            node = queue.pop(0)

            if node in visited:
                return

            # check conditions
            if node == dst:
                return True

            # if not found check its children
            children = self.nodes[node]
            if children:
                for child in children:
                    queue.append(child)

        return False



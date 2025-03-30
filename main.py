from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        
        print(self.ROW)

    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        print(visited)
        queue = []
        queue.append(s)
        visited[s] = True

        print(queue)

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:

                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):

        parent = [-1]*(self.ROW)

        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")

            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s][s]])
                s = parent[s]
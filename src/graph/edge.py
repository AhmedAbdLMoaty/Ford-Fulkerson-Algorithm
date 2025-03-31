class Edge:
    def __init__(self, from_node, to_node, capacity):
        self.from_node = from_node
        self.to_node = to_node
        self.capacity = capacity
        self.flow = 0
        self.reverse = None

    def residual_capacity(self):
        return self.capacity - self.flow
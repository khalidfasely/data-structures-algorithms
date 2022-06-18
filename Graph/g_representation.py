class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        for edge in self.edges:
            edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        
        #The first None ???
        
        adjacency_list = []
        for node in self.nodes:
            #Name it differently
            node_from = []
            for edge in node.edges:
                if (edge.node_from.value == node.value):
                    node_from.append((edge.node_to.value, edge.value))
            if node_from == []:
                adjacency_list.append(None)
            else:
                adjacency_list.append(node_from)
        return adjacency_list
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        """for node_column in self.nodes:
            for node_row in self.nodes:
                for edge_c in node_column.edges:
                    for edge_r in node_row.edges:
                        print(edge_c, edge_r)
            print('###')"""
        """for node in self.nodes:
            print(node.value)
            for edge in node.edges:
                print(edge.value, end="-")
            print()"""
        adjacency_matrix = []
        for node_a in self.nodes:
            edges_list = []
            for node_b in self.nodes:
                #print(node_a.value, '**', node_b.value)
                if node_a.value == node_b.value:
                    #Insert 0 to the tuple
                    edges_list.append(0)
                    #print(0)
                else:
                    num = 0
                    for edge_a in node_a.edges:
                        for edge_b in node_b.edges:
                            if edge_a.value == edge_b.value:
                                # check if node a from is equal edge a from
                                if edge_a.node_from.value == node_a.value:
                                    #print(1, edge_a.value)
                                    num = edge_a.value
                                    #edges_list.append(edge_a.value)
                                #else:
                                #    #print(0)
                                #    edges_list.append(0)
                    edges_list.append(num)
                    #print(num)
            adjacency_matrix.append(edges_list)
        """for node_column in self.nodes:
            print(node_column.value)
            for node_row in self.nodes:
                if (node_column.value == node_row.value):
                    print(0) #if they are connected with some edges # if they are the same nodes
                else:
                    edge = 0
                    for edge_c in node_column.edges:
                        for edge_r in node_row.edges:
                            if edge_r.node_from.value == edge_c.node_to.value:# or edge_r.node_to.value == edge_c.node_from.value:
                                edge = 1 #edge_c.value #edge_r.value
                    # check if they are connected some way from one to another
                    # if node_column.edges.node_to.value == node_row.edges.node_from.value
                        # edge valuef
                    # else: 0
                    ###print(node_column.value, node_row.value)
                    print(edge)
            print('###')///
            #print(node.value)
            ///for edge in self.edges:
                print(edge.value)
                for edge in node.edges:
                    print('node edge', edge.value, end=" ")
                print('/')"""
#            for edge in node.edges:
#                print(node.value, edge.value)
        return adjacency_matrix

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
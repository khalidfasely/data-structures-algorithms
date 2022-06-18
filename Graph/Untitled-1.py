for node_column in self.nodes:
            for node_row in self.nodes:
                if (node_column.value == node_row.value):
                    print(0) #if they are connected with some edges
                else:
                    print(node_column.value, node_row.value)
                    for edge_c in node_column.edges:
                        for edge_r in node_row.edges:
                            if (edge_c.node_from == edge_r.node_to):
                                print('fount connection at ', edge_c.value, edge_r.value)
                    #    print(edge.value, end="-")
                    #print('')
                    #for edge in node_row.edges:
                    #    print(edge.value, end="-")
                    #print('')
                    
            print('###')
            #print(node.value)
            """for edge in self.edges:
                print(edge.value)
                for edge in node.edges:
                    print('node edge', edge.value, end=" ")
                print('/')"""
#            for edge in node.edges:
#                print(node.value, edge.value)
        return []

class Graph:
    """Class to represent a Graph, as a list of weighted nodes and edges."""


    def __init__(self) :
        """Function to initialize a Graph object"""
        pass

    def add_node(self, node_id, weight) : 
        """Function to add a node to a Graph object.
        
        Parameters
        ----------
        node_id : variable representing the ID of a node in the graph.
        
        weight : variable representing the weight of a node in the graph.
        
        You are free to choose your own way to represent nodes and edges.
        """
        pass

    def add_edge(self, source_id, end_id, weight) : 
        """Function to add an edge to a Graph object.
        
        Parameters
        ----------
        source_id : variable representing the ID of the source node of the edge.

        end_id : variable representing the ID of the end node of the edge.
        
        weight : variable representing the weight of an edge in the graph.
        
        You are free to choose your own way to represent nodes and edges.
        """
        pass


def build_Graph(nodes, edges) :
    """Function to build a Graph object from the input data.
    
    Parameters
    ----------
    nodes : list of nodes, each represented as node_id, and node_weight.

    edges : list of edges, each represented as source_node_id, end_node_id, edge_weight.

    Return
    ----------
    A Graph object.
    """

    G = Graph()

    for n in nodes : 
        # n[0] = node id
        # n[1] = node weight
        aux = n.split(', ')
        aux = [int(aux[0]), int(aux[1])]
        G.add_node(aux[0], aux[1])

    for e in edges : 
        # e[0] = source node id
        # e[1] = end node id
        # e[2] = edge weight
        aux = e.split(', ')
        aux = [int(aux[0]), int(aux[1]), int(aux[2])]
        G.add_edge(aux[0], aux[1], aux[2])    

    return G


def print_output(nodes) : 
    """Function to print the shortest path between the two nodes with the highest weigths.

    Parameters
    ----------
    nodes : list of node IDs. For example: nodes = [3, 4, 9]
    """
    aux = '->'.join([str(n) for n in nodes])
    print(aux)


def find_center(G) :
    """Function to find the most central node of a Graph.
    
    Parameters
    ----------
    G : an object representing a Graph.

    Return
    ----------
    The ID of the most central node.
    """
    pass


if __name__ == '__main__':

    # Read the input
    # The first line is made of a list of nodes, written as node_id, node_weight, separated by ;
    nodes = input().split('; ')
    # The second line is made of edges, written as source_node_id, end_node_id, edge_weight, separated by ;
    edges = input().split('; ')

    # Build a directed graph from the input nodes and edges
    G = build_Graph(nodes, edges)

    ### TASK 2 ###
    # Task 2: find the most central node in a graph. The central node is unique.
    
    # Find the center of the Graph
    c = find_center(G)
    
    print(str(c))
    #############


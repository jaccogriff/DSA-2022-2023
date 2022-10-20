from gettext import find
from hashlib import new


class Edge:
    def __init__(self, source, end, weight) :
        self.source = source
        self.end = end
        self.weight = weight

class Node:
    def __init__(self, node, weight) :
        self.id = node
        self.weight = weight

class Graph:
    nodes = []
    edges = []

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
        self.nodes.append( Node(node_id, weight) )

    def add_edge(self, source_id, end_id, weight) : 
        """Function to add an edge to a Graph object.
        
        Parameters
        ----------
        source_id : variable representing the ID of the source node of the edge.

        end_id : variable representing the ID of the end node of the edge.
        
        weight : variable representing the weight of an edge in the graph.
        
        You are free to choose your own way to represent nodes and edges.
        """
        self.edges.append( Edge(source_id, end_id, weight) )



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


def print_output(edges) : 
    """Function to print the minimum spanning tree. In this example, the MST is represented as a list of edges.

    Parameters
    ----------
    MST : the minimum spanning tree, represented as a Graph object or a list of edges.

    If you represent the MST as a Graph object, you can define a print_graph function in the Graph class that prints out the graph, represented as a list of edges (source_id, end_id, weight; source_id, end_id, weight; ...)
    """
    # The expected output is a list of edges, separated by a semicolon, and printed as follow:
    # souce_id, end_id, edge_weight; souce_id, end_id, edge_weight; ...
    for edge in edges[:-1]:
        print(f'{edge.source}, {edge.end}, {edge.weight}', end="; ")
    last_edge = edges[-1]
    print(f'{last_edge.source}, {last_edge.end}, {last_edge.weight}')

def use_weight(edge):
    return edge.weight

def find_set(node, parent):
    if parent[node] != node:
        return find_set (parent[node], parent)
    else:
        return node

def union_set(node_x, node_y, parent):
    parent[find_set(node_y, parent)] = find_set(node_x, parent)

def edge_forms_cycle(edge, parent):
    return find_set(edge.source,parent) == find_set(edge.end, parent)


def minimum_spanning_tree(G) :
    """Function to find the minimum spanning tree of a Graph.
    
    Parameters
    ----------
    G : an object representing a Graph.

    Return
    ----------
    Can either be a subgraph (represented as a Graph object) or a list of edges (source_id, end_id, weight)
    """
    G.edges.sort(key=use_weight)

    mst = []

    parent = {}
    for a_node in G.nodes:
        parent[a_node.id] = a_node.id


    for an_edge in G.edges:

        if edge_forms_cycle(an_edge, parent):
            pass
        else:
            union_set(an_edge.source, an_edge.end, parent)
            mst.append(an_edge)

    return mst



if __name__ == '__main__':

    input1 = "0, 5; 1, 2; 2, 1; 3, 8; 4, 7"
    input2 = "0, 4, 3; 1, 2, 9; 2, 4, 5; 2, 3, 2; 3, 4, 4"

    # Read the input
    # The first line is made of a list of nodes, written as node_id, node_weight, separated by ;
    nodes = input1.split('; ')
    # The second line is made of edges, written as source_node_id, end_node_id, edge_weight, separated by ;
    edges = input2.split('; ')

    # Build a directed graph from the input nodes and edges
    G = build_Graph(nodes, edges)

    ### TASK 3 ###
    # Task 4: find the minimum spanning tree of the Graph.
 
    MST = minimum_spanning_tree(G)
    print_output(MST)
    #############

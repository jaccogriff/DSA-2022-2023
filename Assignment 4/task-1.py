# DSA Student 139


from __future__ import print_function
from cmath import inf, sqrt
import math

class Graph:
    """Class to represent a Graph, as a list of weighted nodes and edges."""
    weight_by_vertices = dict()
    end_nodes_and_weight_by_start_node = dict()
    max_vertex = (-1,0)
    second_max_vertex = (0,-1)

    def __init__(self) :
        """Function to initialize a Graph object"""
        self.weight_by_vertices[(-1,0)] = -1
        self.weight_by_vertices[(0,-1)] = -1

    def add_node(self, node_id, weight) : 
        """Function to add a node to a Graph object.
        
        Parameters
        ----------
        node_id : variable representing the ID of a node in the graph.
        
        weight : variable representing the weight of a node in the graph.
        
        You are free to choose your own way to represent nodes and edges.
        """

        if weight > self.weight_by_vertices[self.max_vertex]:
            self.second_max_vertex = self.max_vertex
            self.max_vertex = node_id
        elif weight > self.weight_by_vertices[self.second_max_vertex]:
            self.second_max_vertex = node_id

        self.weight_by_vertices[node_id] = weight


    def add_edge(self, source_id, end_id, weight) : 
        """Function to add an edge to a Graph object.
        
        Parameters
        ----------
        source_id : variable representing the ID of the source node of the edge.

        end_id : variable representing the ID of the end node of the edge.
        
        weight : variable representing the weight of an edge in the graph.
        
        You are free to choose your own way to represent nodes and edges.
        """
        if source_id in self.end_nodes_and_weight_by_start_node:
            self.end_nodes_and_weight_by_start_node[source_id].append( (end_id, weight) )
        else:
            self.end_nodes_and_weight_by_start_node[source_id] = [(end_id, weight)] 


def build_Graph(nodes, edges) :
    """Function to build a grid-like Graph object from the input data.
    
    Parameters
    ----------
    nodes : list of nodes, each represented as coordinates, and node_weight.
    For example: x1, y1, weight; x2, y2, weight; ...
    edges : list of edges, each represented as source and end node coordintates, and edge_weight.
    For example: x1, y1, x2, y2, weight; x3, y3, x4, y4, weight; ...

    Return
    ----------
    A Graph object.
    """
    G = Graph()

    for n in nodes : 
        aux = n.split(', ')

        temp1 = int(aux[0])
        temp2 = int(aux[1])
        temp_node = (temp1, temp2)

        G.add_node(temp_node, weight=int(aux[2]))

    for e in edges : 
        aux = e.split(', ')

        temp1 = int(aux[0])
        temp2 = int(aux[1])
        temp = (temp1, temp2)

        auxn1 = int(aux[2])
        auxn2 = int(aux[3])
        auxn = (auxn1, auxn2)

        G.add_edge(temp, auxn, weight=int(aux[4]))    

    return G


def print_output(nodes) : 
    """Function to print the shortest path between the two nodes with the highest weigths.
    Parameters
    ----------
    nodes : list of list of nodes (represented as: tuples of coordinates).
    """

    for node in nodes[:-1]:
        print(f'{node[0]}, {node[1]}', end="->")
    
    last_node = nodes[-1]
    print(f'{last_node[0]}, {last_node[1]}')
    # nodes = [x1, y1, x2, y2, x3, y3]
    # Expected output: x1, y1->x2, y2->x3, y3


def astar_shortest_path(G, source_id, end_id, heuristic) : 
    """Function to return the shortest path between two nodes in a Graph.
    
    Parameters
    ----------
    G : object representing a Graph.

    source_id : variable representing the ID of the source node.

    end_id : variable representing the ID of the end node.

    heuristic : heuristic function to compute the distance between two nodes.

    Return
    ----------
    A list of nodes (represented as: x1, y1, weight; x2, y2, weight; ...).
    
    """
    current_node_id = source_id
    explored_nodes = [source_id]

    distance_to_start_node = 0
    while current_node_id != end_id:
        
        h_distance = float(inf)
        neighbor_node_id = None

        for neighbor_node in G.end_nodes_and_weight_by_start_node[current_node_id]:
            distance = heuristic(neighbor_node[0], end_id) + neighbor_node[1] + distance_to_start_node

            if distance < h_distance: 
                h_distance = distance
                current_node_id = neighbor_node[0]

        explored_nodes.append(current_node_id)
        #print(explored_nodes)
        
    return explored_nodes



def heuristic(a, b) : 
    """Function to compute the Euclidean distance between two nodes.
    
    Parameters
    ----------
    a : first node (x1, y1).

    b : second node (x2, y2).

    heuristic : heuristic function to compute the distance between two nodes.

    Return
    ----------
    The distance as an integer.
    """
    a_part_1 = b[0] - a[0]
    b_part_1 = b[1] - a[1]

    a_part = a_part_1 ** 2
    b_part = b_part_1 ** 2

    raw = math.sqrt(
            (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
        ) 
    #print("heuristic -->",raw, "inputs -->", a, b)

    return int(raw)

    # Compute and return the Euclidean distance between a and b


if __name__ == '__main__':

    # Read the input
    # The first line is made of a list of nodes, written as tuples of cartesian coordinates.
    # For example: x1, y1, weight; x2, y2, weight; ...
    # In the previous example, x1, y1, weight; is the first node

    
    nodes = input().split('; ')
    # The second line is made of edges, written as source and end node coordinates, and edge_weight.
    # For example: x1, y1, x2, y2, weight; x3, y3, x4, y4, weight; ...
    # In the previous example, x1, y1, x2, y2, weight; is the first edge
    edges = input().split('; ')

    # Build a grid graph from the input nodes and edges
    G = build_Graph(nodes, edges)

    ### TASK 1 ###
    # Task 1: given a grid-like weighted graph, find the shortest path between the two nodes with max weight. 
    # Because of the grid structure of the graphs, you must implement A*. The heuristic to use is the Euclidean distance between the source and the end node of the shortest path.
    # We always assume there is a path between the two nodes, and all nodes have different weight.

    # Find the two nodes with the highest weights in the graph
    source_id = G.max_vertex
    end_id = G.second_max_vertex

    # Compute the path between the two nodes with the highest weight
    # The source node is the one with the highest weigth
    # You are free to customize the following function
    s_path = astar_shortest_path(G, source_id, end_id, heuristic)

    # Expected output format: list of list of nodes (represented as: tuples of coordinates).
    # For example: x1, y1->x2, y2->x3, y3
    print_output(s_path)


    #############


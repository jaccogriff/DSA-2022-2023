from platform import node
from typing import List

stack = []

def output():
    '''
    Will print the path stored in the `stack` global variable.
    You are free to modify it to be a parameter.
    '''
    for id in stack[:-1]:
        print(f'{id}->', end='')
    try:
        print(f'{stack[-1]}')
    except IndexError:
        pass

def find_path(graph, start, target):
    nodes_by_visitation = {}
    for key in graph.keys():
        nodes_by_visitation[key] = False
    
    nodes_by_visitation[start] = True
    queue = [start]
    parents = {}

    while queue:
        current_node = queue.pop(0)

        if current_node == target:
            break


        for a_neighbour in graph[current_node]:
            if nodes_by_visitation[a_neighbour] == False:  
                queue.append(a_neighbour)
                nodes_by_visitation[a_neighbour] = True
                parents[a_neighbour] = current_node

    child = target
    while child != start:
        stack.append(child)
        child = parents[child]
    stack.append(child)
    stack.reverse()

if __name__ == '__main__':

    input1 = "1, 2; 2, 3; 3, 4; 4, 5; 5, 1"
    input2 = "200000->202000"
    start, target = [int(x) for x in input().split('->')]

    data   = input()
    data_l: List = data.split('; ')
    graph = {}

    for d in data_l:
        id, followers = d.split(', ', 1)
        following_l: List = followers.split(', ')
        
        id = int(id)
        graph[id] = set()

        for f in following_l:
            if f == '':
                # node is not following other nodes.
                continue 
            else:
                f = int(f)
                graph[id].add(f)
                if not graph.get(f):
                    graph[f] = set()

                
    

    '''
    TODO: Step 3: Call your 'find_path` function with the parameters you defined.
    '''
    find_path(graph, start, target)
    
    '''
    TODO: Step 4: Use the `output` function to print your result to stdout.
    '''
    output()                            
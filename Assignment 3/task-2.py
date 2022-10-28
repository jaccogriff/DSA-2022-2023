from typing import List

def stringify_path(path: List):
    '''
    Build string to print
    '''
    ret = ''
    for id in path[:-1]:
        ret = f'{ret}{id}->'
    try:
        ret = f'{ret}{path[-1]}'
    except IndexError:
        pass

    return ret

def output(paths: List[List]):
    '''
    Prints all paths from the list in param
    '''
    paths_string = []
    for p in paths:
        paths_string.append(stringify_path(p))
    print(*paths_string, sep='\n')

'''
DO NOT CHANGE ABOVE
'''

def find_paths() -> List[List]:
        '''
        TODO: Step 2: Implement the multi-path finding method with backtracking.
        Add the parameters you need.

        It is expected to return a List of Lists with the discovered paths.
        For each path a vertice can be visited only once.
        '''

        raise NotImplemented

if __name__ == '__main__':

    '''
    Fetch starting and target node.
    '''
    start, target = [int(x) for x in input().split('->')]

    '''
    Fetch `;` separated twitter data. <id-1: str>, <follower_1-2: str>, ..<follower_1-2: str>; ... 
    i.e: 1, 2, 3; 2, 3, 1; 3, 2
    '''
    data = input()
    data = data.split('; ')

    for d in data:
        id, followers = d.split(', ', 1)
        following_l: List = followers.split(', ')
        graph = {}

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
        TODO: Step 1: Create and store the graph.
            The dataset gives you the IDs of the following.
            Meaning that in the above example:
                `1` is following `2, 3`
                `2` is following `3, 1`
                `3` is following `2`

            As such, the directed Graph's edges (links) derived from the above input will be:
                1->2, 1->3
                2->3, 2->1
                3->2
            
            It is also possible for a user to not be following anyone, see the examples on DomJudge.
        '''


    '''
    TODO: Step 3: Call your 'find_paths` function with the parameters you defined.
    '''
    paths: List[List] = find_paths()

    '''
    Print the paths.
    '''
    output(paths)
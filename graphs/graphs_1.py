#One data type is ideal for representing graphs in Python, i.e. dictionaries

'''
The keys of the dictionary above are the nodes of our graph.
The corresponding values are lists with the nodes, which are connecting by an edge. 
There is no simpler and more elegant way to represent a graph. 
An edge can be seen as a 2-tuple with nodes as elements, i.e. ("a","b") 
'''

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges



#The following Python function calculates the isolated nodes of a given graph:
def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            #isolated += node #same as append
            isolated.append(node)
    return isolated

if __name__ == "__main__":

    graph = { "a" : ["c"], "b" : ["c", "e"], "c" : ["a", "b", "d", "e"], "d" : ["c"], "e" : ["c", "b"], "f" : [] }

    print('List of edges:',end=" ")
    print(generate_edges(graph))
    print('List of isolated edges:',end=" ")
    print(find_isolated_nodes(graph))
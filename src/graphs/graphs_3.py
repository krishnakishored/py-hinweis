from graphs import Graph

g = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

complete_graph = { 
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
}

isolated_graph = { 
    "a" : [],
    "b" : [],
    "c" : []
}


graph = Graph(g)
print(graph.density())

graph = Graph(complete_graph)
print(graph.density())

graph = Graph(isolated_graph)
print(graph.density())


print('#############################################')


g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
}

g2 = { "a" : ["d","f"],
       "b" : ["c"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

g3 = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}


graph = Graph(g)
print(graph)
print(graph.is_connected())

graph = Graph(g2)
print(graph)
print(graph.is_connected())

graph = Graph(g3)
print(graph)
print(graph.is_connected())

print('diameter: ',end='')
diameter = graph.diameter()
print(diameter)
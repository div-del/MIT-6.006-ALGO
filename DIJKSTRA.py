

def create_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    print(graph)
    return graph
   
    
unvisited=["A","B","C","D","E","F"]
visited=[]

vertices=['A', 'B', 'C', 'D', 'E', 'F']
edges=[('A', 'B', 2), ('A', 'D', 8), ('B', 'D', 5), ('B', 'E', 6), ('D', 'E', 3), ('D', 'F', 2), ('C', 'E', 9), ('C', 'F', 3), ('E', 'F', 1)]
graph=create_graph(vertices, edges)

def dijkstras(graph, start_vertex):
    D={vertex: float('inf') for vertex in graph}
    D[start_vertex] = 0
    unvisited=[]
    unvisited=vertices
    visited=[]
    while unvisited:
        min_vertex=None
        for vertex in unvisited:
            if min_vertex==None:
                min_vertex=vertex
            elif D[vertex]<D[min_vertex]:
                min_vertex=vertex
        vertex=min_vertex

        
        if D[vertex]!=float('inf'):
            for neighbor,weight in graph[vertex]:
                if D[vertex]+weight < D[neighbor]:
                    D[neighbor]=D[vertex]+weight
        visited.append(vertex)
        unvisited.remove(vertex)
        if not unvisited:
            break
    print(D)
print()      
dijkstras(graph, "A")

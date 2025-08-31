def create_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    return graph
    

def bfs(graph, start, end):
    parent = {}
    visited = set()
    queue = [start]
    
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        #print("before ",queue)
        ##print(vertex, end=" ")
        if vertex==end:
            break
        for neighbor in graph[vertex]:
            #print("neighbor ", neighbor)
            if neighbor not in visited:
                parent[neighbor]=vertex
                visited.add(neighbor)
                queue.append(neighbor)
                #print("after ",queue)
    print(parent)
    X=end
    L=[]
    while vertex!=start:
        L+=[X,]
        X=parent[X]
        vertex=X
        if X==start:
            L+=[X,]
            break
    L.reverse()
    print(L)


# Example usage
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
               



graph = create_graph(vertices, edges)

print("BFS from  A to F:")
bfs(graph, 'A', 'F')




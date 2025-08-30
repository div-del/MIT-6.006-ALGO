
def create_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs(graph, start):
    visited = set()
    queue = [start]
    
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        print(queue)
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(queue)

vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
graph = create_graph(vertices, edges)

print("BFS traversal starting from vertex A:")
bfs(graph, 'A')




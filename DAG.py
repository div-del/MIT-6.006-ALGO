
def create_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    return graph
    
def topological_sort_util(graph, vertex, visited, stack):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        j=neighbor[0]
        #print("aha ",neighbor)
        if j not in visited:
            #print(neighbor)
            topological_sort_util(graph, j, visited, stack)
    stack.append(vertex)  
    #print("stack ",stack)
    #print("OUT")
    #print()

def topological_sort(graph):
    stack = []
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            #print("vertex",vertex)
            topological_sort_util(graph, vertex, visited, stack)
    k=stack[::-1]
    return k
def DAG(graph, stack, start_vertex):
    # Step 1: Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0

    # Step 2: Iterate through vertices in topological order
    for vertex in stack:
        # Step 3: Relax all outgoing edges
        # The 'if' is a crucial check to avoid relaxing from an unreachable vertex
        if distances[vertex] != float('inf'):
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    
    return distances


print()
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4)],
    'C': [('D', 1), ('E', -1)],
    'D': [('E', 5)],
    'E': []
}
k=topological_sort(graph)
print("Topological Sort: ", k)
min_path=DAG(graph, k, "A")
print("Minimum path from source A: ", min_path)
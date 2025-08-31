
def create_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    return graph
    

def dfs(graph, start):
    parent = {}
    visited = set()
    stack = [start]
    
    visited.add(start)
    while stack:
        vertex = stack.pop()
        #print("before ",queue)
        print(vertex, end=" ")
        ##if vertex==end:
          #  break
        K=graph[vertex][::-1]
        for neighbor in K:
            #print("neighbor ", neighbor)
            if neighbor not in visited:
                ###parent[neighbor]=vertex
                
                visited.add(neighbor)
                stack.append(neighbor)
                #print("after ",queue)
    

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
               



graph = create_graph(vertices, edges)

print("DFS from  A :")
dfs(graph, 'A')

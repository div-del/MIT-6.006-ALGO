
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
    k=[]
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
graph={
'A': ['B'],
'B': ['C', 'D'],
'C': ['E', 'F'],
'D': ['B', 'E', 'F'],
'E': ['C', 'D'],
'F': ['D', 'E']
}
print("DFS from  A :")
dfs(graph, 'A')

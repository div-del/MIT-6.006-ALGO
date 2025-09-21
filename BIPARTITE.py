
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
    red=set()
    blue=set()
    red.add(start)
    K=0
    is_bipartite = True
    while stack:
        vertex = stack.pop()
        if vertex in red:
            current_set = red
            neighbor_set = blue
        else:
            current_set = blue
            neighbor_set = red


        
        
        for neighbor in graph[vertex]:
            
        
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor_set.add(neighbor)
                stack.append(neighbor)
            else:
                if neighbor in current_set:
                    is_bipartite = False
                    break
        if not is_bipartite:
            break
        
    
    if is_bipartite:
        print("Bipartite")
        print("Red set:", red)
        print("Blue set:", blue)
    else:
        print("Not Bipartite")
                
                
             
    
    

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'F'),
    ('E', 'F')
]




graph = create_graph(vertices, edges)


dfs(graph, 'A')

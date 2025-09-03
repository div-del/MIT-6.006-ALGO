
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
def DAG(graph, stack, vertex):
    for v in stack:
        for neighbor in graph[vertex]:
            j=neighbor[0]

#print("DFS from  A :")
#dfs(graph, 'A')

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
DAG(graph, k)
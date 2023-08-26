from collections import deque

graph= { 'a':['b','c'],
         'b':['d','e'],
         'c':['f'],
         'd':[],
         'e':[],
         'f':[]
        } 

# BFS --Code

visited=[]
def bfs(start, graph):
    queue=[]
    queue.append(start)
    visited.append(start)
    print(start)
    while queue:
        front=queue.pop(0)
        for child in graph[front]:
            if child not in visited:
                print(child)
                visited.append(child)
                queue.append(child)
visited=[]
def dfs(start, graph):
    stack=deque()
    stack.append(start)
    visited.append(start)
    print(start)
    while stack:
        front=stack.pop()
        for child in graph[front]:
            if child not in visited:
                print(child)
                visited.append(child)
                stack.append(child)
def topological_sort(graph, vertex, visited, stack):
    visited.append(vertex)
    if vertex in graph:
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                topological_sort(graph,neighbour,visited,stack)
    stack.append(vertex)



def get_topological_sort(graph):
    visited=[]
    stack=[]
    for vertex in graph:
        if vertex not in visited:
            topological_sort(graph,vertex,visited,stack)
    return stack[::-1]

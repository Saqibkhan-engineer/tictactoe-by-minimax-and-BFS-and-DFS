from collections import deque

graph = {
    'Karachi': ['Lahore', 'Faisalabad'],
    'Peshawar': ['Islamabad', 'Quetta'],
    'Quetta': ['Peshawar'],
    'Multan': ['Lahore', 'Faisalabad'],
    'Faisalabad': ['Karachi', 'Multan'],
    'Lahore': ['Islamabad', 'Karachi', 'Multan'],
    'Islamabad': ['Lahore', 'Peshawar']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" -> ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" -> ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("BFS starting from Karachi")
bfs(graph, 'Karachi')
print("\n")
print("DFS starting from Karachi")
dfs(graph, 'Karachi')

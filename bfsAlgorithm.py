from collections import deque
def bfs(adj, s):
    # Create a queue for BFS
    q = deque()
    
    visited = [False] * len(adj);
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        curr = q.popleft();
        print(curr, end=" ")
      
        # Dequeue a vertex from queue and print it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    V = 5

    # Adjacency list
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0)
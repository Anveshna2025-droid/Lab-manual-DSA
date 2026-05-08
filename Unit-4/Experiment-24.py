# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 24
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement Breadth-First Search (BFS) on a graph to explore nodes level-by-level.

# Input / Output expectation
# Input: A starting node for traversal.
# Output: A list of nodes in the order they were visited during BFS.

#<=====================CODE STARTS==========================>

from collections import deque

class GraphBFS:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        # Building an undirected graph for traversal
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def perform_bfs(self, start_node):
        # Set to keep track of visited nodes
        visited = {start_node}
        # Queue for BFS (FIFO)
        queue = deque([start_node])
        traversal_order = []

        while queue:
            # Dequeue a vertex from queue
            current_vertex = queue.popleft()
            traversal_order.append(current_vertex)

            # Get all adjacent vertices of the dequeued vertex
            # If a neighbor has not been visited, mark it visited and enqueue it
            for neighbor in self.adj_list.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return traversal_order

def main():
    print("--- BREADTH-FIRST SEARCH (BFS) ANALYSIS ---")
    g = GraphBFS()
    
    # Defining a sample network
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
    for u, v in edges:
        g.add_edge(u, v)
    
    start = 'A'
    result = g.perform_bfs(start)
    
    print(f"Starting Node: {start}")
    print(f"BFS Traversal Order: {result}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(V + E) - Every vertex and edge is explored once.")
    print("2. Space Complexity: O(V) - Required for the visited set and the queue.")
    print("3. Mechanism: Uses a Queue (FIFO) to explore neighbors before going deeper.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
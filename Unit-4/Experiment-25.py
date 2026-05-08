# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 25
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement Depth-First Search (DFS) on a graph using recursion.

# Input / Output expectation
# Input: A starting node for traversal.
# Output: A list of nodes in the order they were visited during DFS.

#<=====================CODE STARTS==========================>

class GraphDFS:
    def __init__(self):
        # Using a dictionary for the Adjacency List
        self.adj_list = {}

    def add_edge(self, u, v):
        # Adding edges for an undirected graph
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def perform_dfs(self, start_node):
        visited = set()
        traversal_order = []
        
        # Helper function for recursion
        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            
            # Explore each neighbor that hasn't been visited yet
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_node)
        return traversal_order

def main():
    print("--- DEPTH-FIRST SEARCH (DFS) ANALYSIS ---")
    g = GraphDFS()
    
    # Defining the same network structure as BFS for comparison
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
    for u, v in edges:
        g.add_edge(u, v)
    
    start = 'A'
    result = g.perform_dfs(start)
    
    print(f"Starting Node: {start}")
    print(f"DFS Traversal Order: {result}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(V + E) - Visits all vertices and edges.")
    print("2. Space Complexity: O(V) - Due to the recursion stack and visited set.")
    print("3. Mechanism: Uses Recursion (LIFO logic) to go as deep as possible.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
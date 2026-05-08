# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 23
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Represent a directed weighted graph using an adjacency list.

# Input / Output expectation
# Input: Nodes and edges with weights.
# Output: Readable adjacency list representation showing nodes and their weighted connections.

#<=====================CODE STARTS==========================>

class WeightedGraph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adj_list = {}

    def add_node(self, node):
        # Add a node to the graph if it doesn't already exist
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight):
        # Ensure both source and destination nodes exist in the graph
        self.add_node(u)
        self.add_node(v)
        # Add a directed edge from u to v with the specified weight
        self.adj_list[u].append((v, weight))

    def display(self):
        print("--- ADJACENCY LIST REPRESENTATION ---")
        print("Format: Node -> [(Neighbor, Weight), ...]\n")
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

def main():
    g = WeightedGraph()
    
    # Requirement: Using 5–7 nodes and 8–10 edges as per manual
    edges = [
        ('A', 'B', 10), ('A', 'C', 12),
        ('B', 'C', 5),  ('B', 'D', 8),
        ('C', 'E', 3),  ('D', 'E', 7),
        ('D', 'F', 2),  ('E', 'F', 6),
        ('A', 'D', 15)
    ]
    
    # Insert the edges into the graph
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    # Display the final structure
    g.display()

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Space Complexity: O(V + E) - Efficiently stores vertices and edges.")
    print("2. Time Complexity (Adding Edge): O(1) - Constant time insertion.")
    print("3. Advantage: Highly efficient for representing sparse graphs.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
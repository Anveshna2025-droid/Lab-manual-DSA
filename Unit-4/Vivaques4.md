# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Unit 4 Viva Preparation: Non-Linear & Advanced Data Structures
# Submitted to = Deepak Kaushik Sir
# <=========================================>

### 5.1. Experiment 20: BST Insert/Search/Inorder
1. **Why inorder gives sorted?**
   - Because Inorder follows $Left \to Root \to Right$. In a BST, all smaller elements are on the left and larger on the right, so visiting them in this sequence naturally yields sorted order.

2. **Worst-case BST height?**
   - **$O(n)$.** This happens when elements are inserted in sorted order (ascending or descending), creating a "skewed tree" that looks like a Linked List.

3. **Average complexity?**
   - **$O(\log n)$** for both insertion and searching, assuming the tree is relatively balanced.

---

### 5.2. Experiment 21: BST Delete (All Cases)
1. **Inorder successor meaning?**
   - It is the node with the smallest value in the right subtree of the node to be deleted. It is the next immediate value in sorted order.

2. **Why delete is tricky?**
   - Because deleting a node with two children requires restructuring the tree to maintain the BST property without losing the subtrees.

3. **How to verify correctness?**
   - By performing an **Inorder Traversal** after the deletion. If the output remains sorted and the specific node is missing, the operation was successful.

---

### 5.3. Experiment 22: Heap / Priority Queue
1. **Why heap for priority queues?**
   - Heaps provide $O(1)$ access to the highest (or lowest) priority element and $O(\log n)$ efficiency for updates, which is faster than a sorted array or list.

2. **Insert/extract complexity?**
   - Both insertion and extraction take **$O(\log n)$** time due to the "heapify" process required to maintain the tree structure.

3. **Where used in industry?**
   - Used in **Operating System Schedulers** (managing process priority), **Dijkstra’s Shortest Path Algorithm**, and **Bandwidth management** in routers.

---

### 5.4. Experiment 23: Graph Build (Adjacency List)
1. **List vs matrix?**
   - **List:** Saves space for sparse graphs ($O(V+E)$).
   - **Matrix:** Faster for checking if a specific edge exists ($O(1)$) but uses more memory ($O(V^2)$).

2. **Directed vs undirected?**
   - In a **Directed** graph, edges have a specific direction ($A \to B \neq B \to A$). In **Undirected**, edges are bidirectional ($A-B$).

3. **Weighted graph use?**
   - Used in **Navigation Maps** (weights represent distance/time) and **Network Routing** (weights represent cost or latency).

---

### 5.5. Experiment 24: BFS Traversal
1. **Why queue in BFS?**
   - BFS explores level-by-level. A queue (FIFO) ensures that nodes discovered first at a certain depth are processed before moving to the next depth.

2. **Shortest path relation?**
   - In an unweighted graph, BFS is guaranteed to find the shortest path (minimum number of edges) between the start node and any other node.

3. **Complexity O(V+E)?**
   - Every vertex (V) is added to the queue once, and every edge (E) is checked to find neighbors, leading to a linear time complexity relative to the graph size.

---

### 5.6. Experiment 25: DFS Traversal
1. **DFS vs BFS?**
   - DFS goes as deep as possible along a branch before backtracking (uses a Stack), while BFS explores all neighbors at the current depth before moving deeper (uses a Queue).

2. **Recursion depth issue?**
   - For very deep or skewed graphs, recursive DFS can cause a **Stack Overflow** error because each call adds a new frame to the system call stack.

3. **Use case of DFS?**
   - **Cycle Detection** in a graph, solving puzzles like **Mazes**, and **Topological Sorting** in compilers.

---

### 5.7. Experiment 26: Hash Table (Separate Chaining)
1. **Collision meaning?**
   - A collision occurs when two different keys result in the same index after being processed by the hash function.

2. **Why chaining works?**
   - It allows multiple elements to exist at the same index by storing them in a Linked List (chain), so no data is overwritten.

3. **Load factor?**
   - It is the ratio $n/m$ (number of elements / number of slots). A high load factor means more collisions and slower performance.

---

### 5.8. Experiment 27: Trie (Prefix Tree)
1. **Trie vs hash map for prefix?**
   - Tries are much faster for prefix searches (like "find all words starting with 'ap'") because they store characters along paths, whereas Hash Maps require checking every key.

2. **Space trade-off?**
   - Tries can use a lot of memory because each node stores multiple pointers (one for every possible character in the alphabet).

3. **Autocomplete use?**
   - When you type in a search bar, a Trie quickly traverses the characters typed so far to suggest all possible word completions in the sub-tree.

---

### 5.9. Experiment 28: Bloom Filter
1. **Can bloom filter have false negatives?**
   - **No.** If the filter says an item is "not present," it is 100% certain. It can only have False Positives.

2. **Why memory efficient?**
   - It uses a simple bit array rather than storing the actual data (strings/objects), allowing it to represent millions of items in a few megabytes.

3. **Industry use?**
   - **Database Caching:** To avoid looking up non-existent keys on a disk. **Google Chrome:** To identify malicious URLs.

# <==================== END OF VIVA PREP ====================>
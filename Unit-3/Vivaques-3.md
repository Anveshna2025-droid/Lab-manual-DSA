# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Unit 3 Viva Preparation: Sorting Algorithms
# Submitted to = Deepak Kaushik Sir
# <=========================================>

### 4.1. Experiment 14: O(n2) Sorts + Counting
1. **Stable vs unstable?**
   - **Stable:** Maintains the relative order of duplicate elements (e.g., Bubble Sort).
   - **Unstable:** Does not guarantee relative order (e.g., Selection Sort).

2. **In-place meaning?**
   - The algorithm sorts the data within the original array without needing extra memory (Space Complexity: O(1)).

3. **Why O(n2) is slow?**
   - Because the number of operations grows quadratically with input size; doubling the data quadruples the work.

---

### 4.2. Experiment 15: Insertion Sort
1. **Worst-case input?**
   - An array sorted in **reverse order**, as every element must be compared and shifted to the very beginning.

2. **Is insertion stable?**
   - **Yes.** It preserves the original order of equal elements because it only shifts elements that are strictly greater.

3. **Space complexity?**
   - **O(1).** It only requires a constant amount of additional memory for its operations.

---

### 4.3. Experiment 16: Merge Sort
1. **Why stable?**
   - During the "merge" step, if two elements are equal, we prioritize the one from the left subarray, keeping their original sequence.

2. **Why needs extra memory?**
   - It requires an auxiliary array of size **O(n)** to temporarily hold and merge the divided elements.

3. **Use in external sorting?**
   - It is highly efficient for data too large for RAM because it can sort chunks of data sequentially from a disk.

---

### 4.4. Experiment 17: Quick Sort
1. **Worst-case for quick sort?**
   - When the pivot is consistently the smallest or largest element (e.g., already sorted data with a fixed pivot), resulting in **O(n2)**.

2. **Is quick sort stable?**
   - **No.** The partitioning involves long-distance swaps that can jump equal elements over each other.

3. **Average time?**
   - **O(n log n).** This occurs when the pivot splits the array into reasonably balanced partitions.

---

### 4.5. Experiment 18: Heap Sort
1. **Why heap sort not stable?**
   - The heapify process and the root-to-end swaps move elements non-sequentially, which disrupts the original order of equal keys.

2. **Heap vs BST for top-k?**
   - **Heap** is better. A Min-Heap of size K can find the top-K elements in O(n log k) with less overhead than a full BST.

3. **Real priority queue use?**
   - Used in **CPU Scheduling**, **Dijkstra’s algorithm** for shortest paths, and network packet management.

---

### 4.6. Experiment 19: Benchmark Harness
1. **Why reverse is worst for insertion?**
   - Because each new element must be compared and shifted past all previously sorted elements to reach its spot at the front.

2. **Why quick may degrade on sorted with bad pivot?**
   - Unbalanced partitions turn the recursive calls into a linear chain of depth N, losing the logarithmic efficiency.

3. **Why merge stable but uses memory?**
   - It guarantees stability through its merge logic but requires O(n) space to rebuild the arrays during the "Divide & Conquer" phase.

# <==================== END OF VIVA PREP ====================>
# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 22
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement a Min-Heap / Priority Queue and verify extraction order.

# Input / Output expectation
# Input: List of priorities (numbers).
# Output: Extracted sequence showing elements removed in increasing order.

#<=====================CODE STARTS==========================>

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        heapq.heappush(self.heap, key)
        print(f"Inserted {key}, Current Heap: {self.heap}")

    def extract_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

def main():
    print("--- HEAP / PRIORITY QUEUE ANALYSIS ---")
    pq = PriorityQueue()
    
    # Implementing Min-Heap for a task scheduler logic
    tasks = [45, 10, 55, 20, 30]
    print(f"Initial Task Priorities: {tasks}\n")
    
    for task in tasks:
        pq.insert(task)
    
    print("\nExtraction Process (Highest Priority First / Min Value):")
    extracted_order = []
    while pq.heap:
        val = pq.extract_min()
        extracted_order.append(val)
        print(f"Extracted: {val} | Remaining Heap: {pq.heap}")
    
    print(f"\nFinal Extracted Sequence: {extracted_order}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Insertion: O(log n) - Maintaining the heap property.")
    print("2. Extraction: O(log n) - Removing the root and heapifying.")
    print("3. Peek (Min): O(1) - The root always holds the minimum value.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
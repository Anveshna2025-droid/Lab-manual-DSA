# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -18
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Use heapify idea to sort in O(n log n) and connect to priority queue concepts.

# Input / Output expectation
# Input: unsorted list.
# Output: sorted list + explanation of stability.

#<=====================CODE STARTS==========================>

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def main():
    print("--- HEAP SORT (MAX-HEAP BRIDGE) ---")
    data = [12, 11, 13, 5, 6, 7]
    print(f"Original Array: {data}")
    
    heap_sort(data)
    print(f"Sorted Array:   {data}")

    print("\n" + "="*35)
    print("COMPLEXITY & LOGIC:")
    print("1. Time Complexity: O(n log n) for all cases.")
    print("2. Space Complexity: O(1) - In-place sorting.")
    print("3. Stability: Unstable - Swaps non-adjacent elements across the heap.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
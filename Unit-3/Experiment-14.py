# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -14
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Understand cost drivers (comparisons/swaps) and quadratic growth in Bubble Sort.

# Input / Output expectation
# Input: list of numbers.
# Output: sorted list + total comparisons + total swaps.

#<=====================CODE STARTS==========================>

def bubble_sort_analysis(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    # Outer loop for each pass
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                
    return arr, comparisons, swaps

def main():
    print("--- BUBBLE SORT ANALYSIS ---")
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original Array: {data}")
    
    sorted_arr, comp, swp = bubble_sort_analysis(data.copy())
    
    print(f"Sorted Array:   {sorted_arr}")
    print(f"Total Comparisons: {comp}")
    print(f"Total Swaps:       {swp}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(n^2) - Nested loops result in quadratic growth.")
    print("2. Space Complexity: O(1) - Sorting is done in-place.")
    print("3. Stability: Stable - Does not change relative order of equal elements.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
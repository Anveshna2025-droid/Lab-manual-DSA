# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -6
# Submitted to = Deepak Kaushik Sir
# <=========================================>


# Aim - Implement binary search recursively and explain why it is O(log n).

# Input / Output expectation
# Input: n.
# Output: move sequence for n=3 + move count for n=4 + complexity statement.

#<=====================CODE STARTS==========================>

def binarySearch(arr, key, low, high):
    
    # Implementation of Recursive Binary Search.
    # Dividing the search interval in half using recursion.
    # Base Case 1: Search range is exhausted (Key not found)
    if low > high:
        print(f"-> Range exhausted: Key {key} NOT FOUND!!")
        return -1
    
    # Safe Mid Calculation: Prevents integer overflow in low-level memory
    mid = low + (high - low) // 2
    
    # Trace: Shows current state for lab verification
    print(f"Trace: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")
    
    # Base Case 2: Key found
    if arr[mid] == key:
        print(f"-> Key {key} found at index {mid}!")
        return mid
    
    # Recursive Case 1: Key is smaller, search the left half
    elif arr[mid] > key:
        return binarySearch(arr, key, low, mid - 1)
    
    # Recursive Case 2: Key is larger, search the right half
    else:
        return binarySearch(arr, key, mid + 1, high)

def main():
    print("=== EXPERIMENT 6: BINARY SEARCH ANALYSIS ===\n")
    
    # Test Data
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Sorted Array: {arr}")
    
    # User Input for searching
    try:
        target = int(input("\nEnter the key to search: "))
        result = binarySearch(arr, target, 0, len(arr) - 1)
        print(f"\nFinal Result: {result}")
    except ValueError:
        print("Invalid input. Please enter a number.")

    # Lab Manual Requirements: Edge Cases & Recurrence
    print("\n[Testing Edge Cases]")
    print(f"Empty List Test: {binarySearch([], 10, 0, -1)}")

    print("\n" + "="*35)
    print("RECURRENCE INTUITION:")
    print("1. Relation: T(n) = T(n/2) + O(1)")
    print("2. T(n/2): The problem size is halved at each step.")
    print("3. O(1): Constant time spent on mid-point calculation.")
    print("4. Complexity: O(log n) Time | O(log n) Space.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
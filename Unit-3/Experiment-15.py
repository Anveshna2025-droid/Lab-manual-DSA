# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -15
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement insertion sort and observe behavior on nearly sorted data.

# Input / Output expectation
# Input: list of numbers.
# Output: sorted list + pass-wise visualization.

#<=====================CODE STARTS==========================>

def insertion_sort(arr):
    print(f"Initial: {arr}")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i}:   {arr}")
    return arr

def main():
    print("--- INSERTION SORT TRACE ---")
    data = [12, 11, 13, 5, 6]
    insertion_sort(data)

    print("\n" + "="*35)
    print("PROPERTIES:")
    print("1. Best Case: O(n) - Occurs when data is already sorted.")
    print("2. Worst Case: O(n^2) - Occurs when data is reverse sorted.")
    print("3. Advantage: Highly efficient for nearly sorted datasets.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
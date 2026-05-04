# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -17
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement quick sort and understand pivot impact on performance.

#<=====================CODE STARTS==========================>

def partition(arr, low, high):
    # Choosing the last element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)
        
        # Separately sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    print("--- QUICK SORT (PARTITION STRATEGY) ---")
    data = [10, 7, 8, 9, 1, 5]
    print(f"Original: {data}")
    quick_sort(data, 0, len(data) - 1)
    print(f"Sorted:   {data}")

    print("\n" + "="*35)
    print("CRITICAL NOTES:")
    print("1. Average Case: O(n log n).")
    print("2. Worst Case: O(n^2) - Occurs with poor pivot (e.g., sorted array + last element pivot).")
    print("3. Stability: Unstable - May change order of equal elements.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -16
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Learn divide & conquer strategy and stable merging with Merge Sort.

#<=====================CODE STARTS==========================>

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Conquer & Combine
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # Maintains stability
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            
    # Append remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def main():
    print("--- MERGE SORT (DIVIDE & CONQUER) ---")
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted: {data}")
    result = merge_sort(data)
    print(f"Sorted:   {result}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(n log n) in all cases.")
    print("2. Space Complexity: O(n) - Requires extra memory for merging.")
    print("3. Paradigm: Divide and Conquer.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -19
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Measure execution time fairly and compare algorithms on different input types.

# Input / Output expectation
# Input: random/sorted/reverse datasets for sizes 1000/5000/10000.
# Output: timing table with comparison data.

#<=====================CODE STARTS==========================>
import time
import random

# Implementation of algorithms to be tested (Minimal versions)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]; j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]; j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def benchmark():
    sizes = [1000, 5000] # Kept smaller for quick lab demo
    types = ["Random", "Sorted", "Reverse"]
    
    print(f"{'Size':<8} | {'Type':<10} | {'Insertion (s)':<15} | {'QuickSort (s)':<15}")
    print("-" * 55)

    for size in sizes:
        for t_type in types:
            # Data Generation
            if t_type == "Random": data = [random.randint(0, 10000) for _ in range(size)]
            elif t_type == "Sorted": data = list(range(size))
            else: data = list(range(size, 0, -1))

            # Benchmark Insertion Sort
            arr_copy = data.copy()
            start = time.time()
            insertion_sort(arr_copy)
            time_ins = time.time() - start

            # Benchmark Quick Sort
            arr_copy = data.copy()
            start = time.time()
            quick_sort(arr_copy)
            time_qs = time.time() - start

            print(f"{size:<8} | {t_type:<10} | {time_ins:<15.5f} | {time_qs:<15.5f}")

def main():
    print("=== EXPERIMENT 19: PERFORMANCE BENCHMARKING ===\n")
    benchmark()
    print("\n" + "="*35)
    print("OBSERVATIONS:")
    print("1. Insertion sort is extremely fast for 'Sorted' data [O(n)].")
    print("2. QuickSort outperforms Insertion Sort significantly as size increases.")
    print("3. Recursive depth may be an issue for very large reverse datasets.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -2 
# Submitted to = Deepak Kaushik Sir
# <=========================================>


# Aim - Develop intuition for time/space complexity using simple loop structures and case analysis

# Input / Output expectation
# Input: n.
# Output: for each snippet print estimated operation count + complexity label + 2-line justification.

#<=====================CODE STARTS==========================>

def complexity_drill():
    print("--- Complexity Drill ---")
    n = int(input("Enter the value for n: "))
    print("-" * 30)

# Snippet-1
# Single Loops (Time Complexity = O(n))
# Represents Linear growth.
    linear_count = 0
    for i in range(n):
          linear_count+= 1
    print(f"\n[O(n)] for Single Loop : {linear_count}")
    print("Justification: The loop runs exactly n times, processing each element once.")
    print("Execution time grows linearly as the input size n increases.")
    print("-" * 30)

# Snippet-2
# Nested Loops (Time Complexity = O(n^2))
# Represents Quadratic growth.
    nested_count = 0
    for i in range(n):
        for j in range(n):
            nested_count+= 1
    print(f"[O(n^2)] for Nested Loop : {nested_count}")
    print("Justification: For every 1 iteration of the outer loop, the inner loop runs n times.")
    print("Total operations equal n * n, representing quadratic growth.")
    print("-" * 30)

# Snippet-3
# Triangluar Loops (Time Complexity = O(n^2))
# This is a nested loop where the inner loop depends on the outer loop.
    trian_count = 0
    for i in range(n):
        for j in range(i, n):
            trian_count+= 1
    print(f"[O(n^2)] for Triangular Loop : {trian_count}")
    print("Justification: The inner loop range decreases with each outer iteration (n, n-1, ..., 1).")
    print("The sum follows [n(n+1)/2], which simplifies to O(n^2) by dropping constants.")
    print("-" * 30)

# Snippet-4
# Halving Loops (Time Complexity = O(log n))
# Represents Logarithmic growth (like Binary Search).
    log_count = 0
    temp_n = n
    while temp_n > 1:
        temp_n //= 2  # Keep dividing by 2
        log_count += 1
    print(f"[O(log n)] for Halving Loop : {log_count}")
    print("Justification: The problem size is divided by 2 in every step until it reaches 1.")
    print("The number of steps required to reduce n to 1 is proportional to log2(n).")
    print("-" * 30)
    
if __name__ == "__main__":
    complexity_drill()

#<=====================CODE ENDS============================>
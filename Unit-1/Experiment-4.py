# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -4
# Submitted to = Deepak Kaushik Sir
# <=========================================>


# Aim - Understand inefficiency of naive recursion and benefit of memoization

# Input / Output expectation
# Input: n values .
# Output: fib(n) + calls naive + calls memo + short explanation (3–4 lines).

#<=====================CODE STARTS==========================>
calls_naive = 0
calls_memo = 0
def fib_naive(n):
    global calls_naive
    calls_naive += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
def fib_memo(n, memo={}):
    global calls_memo
    calls_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
def main():
    global calls_naive, calls_memo
    print("---Naive vs Memoized method ---")
    
    
    test_num = [10, 20, 30]
    
    print(f"{'n':<5} | {'Result':<10} | {'Naive Calls':<15} | {'Memo Calls':<15}")
    print("-" * 35)
    
    for n in test_num:
        # Reset counters
        calls_naive = 0
        calls_memo = 0
        
        # Calculate
        ans = fib_memo(n, {}) # Use fresh memo for each n
        fib_naive(n)
        
        print(f"{n:<5} | {ans:<10} | {calls_naive:<15} | {calls_memo:<15}")

    print("\n" + "="*35)
    print("EXPLANATION:")
    print("1. Naive recursion re-calculates the same subproblems multiple times,leading to exponential time complexity O(2^n).")
    print("2. Memoization stores previously calculated results in a dictionary,reducing the complexity to O(n) by eliminating redundant calls.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>

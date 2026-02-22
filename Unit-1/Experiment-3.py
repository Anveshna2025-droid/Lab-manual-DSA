# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -3 
# Submitted to = Deepak Kaushik Sir
# <=========================================>


# Aim - Learn recursion basics: base case, recursive case, and stack growth

# Input / Output expectation
# Input: n.
# Output:  factorial(n) + manual call stack trace (in notebook) + time/space complexity statement

#<=====================CODE STARTS==========================>

def factorial(n):
    # Base Case: stops at 0 or 1
    if n <= 1:
        return 1
    # Recursive Case: n * (n-1)!
    return n * factorial(n - 1)

def display_stack_trace(n):
    #Printing a visualization of the call stack growth.
    print(f"\n--- Call Stack Trace for factorial({n}) ---")
    for i in range(n, 0, -1):
        print(f"PUSH: factorial({i}) -> Waiting for factorial({i-1})")
    print("BASE CASE: factorial(0) returns 1")
    print("POP: Values returning back up the stack...")
    print("------------------------------------------")

def main():
    u_input = input("Enter a non-negative integer: ").strip()
    n = int(u_input)
    if n < 0:
        print("Invalid Input: n must be greater than or equal to 0 (Factorial of -ve numbers is not defined).")
    else:
            # Display logic
            display_stack_trace(n)
            result = factorial(n)
            
            print(f"FINAL RESULT: {n}! = {result}")
            
            # Lab Manual Requirements
            print("\nCOMPLEXITY EXPLAINED:")
            print(f"1. Time Complexity: O(n) - Function calls itself {n} times.")
            print(f"2. Space Complexity: O(n) - Because the computer must store all {n} calls in memory (the call stack) at the same time before it can start calculating the result. ")

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
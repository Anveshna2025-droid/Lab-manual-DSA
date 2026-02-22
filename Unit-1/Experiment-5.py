# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -5
# Submitted to = Deepak Kaushik Sir
# <=========================================>


# Aim - Use recursion to generate step-by-step solution and observe exponential growth

# Input / Output expectation
# Input: n.
# Output: move sequence for n=3 + move count for n=4 + complexity statement.

#<=====================CODE STARTS==========================>
# Name = Anveshna
# Experiment - 5
# <=========================================>
def hanoi(n, source, auxiliary, destination, print_moves=True):
    # Base Case: Only one disk to move
    if n == 1:
        if print_moves:
            print(f"Move disk 1 from {source} to {destination}")
        return 1
    
    # Step 1: Move n-1 disks from Source to Aux
    count1 = hanoi(n-1, source, destination, auxiliary, print_moves)
    
    # Step 2: Move the nth disk from Source to Destination
    if print_moves:
        print(f"Move disk {n} from {source} to {destination}")
    count2 = 1
    
    # Step 3: Move n-1 disks from Aux to Destination
    count3 = hanoi(n-1, auxiliary, source, destination, print_moves)
    
    # Total moves = (2 * moves for n-1) + 1
    return count1 + count2 + count3

def main():
    print("--- TOWER OF HANOI ---")
    
    # Taking input directly
    n_input = int(input("Enter number of disks to trace (e.g., 3): "))
    
    # Part 1: Trace for the input provided (Required for N=3)
    print(f"\n[PART 1] Move Sequence for n = {n_input}:")
    print("-" * 35)
    total_moves = hanoi(n_input, "A", "B", "C", print_moves=True)
    print(f"\nTotal Moves for n={n_input}: {total_moves}")

    # Part 2: Move count for N=4 (Requirement from Lab Manual)
    print(f"\n[PART 2] Move count for n = 4 (Calculation only):")
    total_4 = hanoi(4, "A", "B", "C", print_moves=False)
    print(f"Total Moves: {total_4}")

    # Part 3: Complexity Statement
    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(2^n)")
    print("2. Space Complexity: O(n) (Depth of recursion stack)")
    print("3. Recurrence Relation: T(n) = 2T(n-1) + 1")
    print("="*35)

if __name__ == "__main__":
    main()
#<=====================CODE ENDS============================>

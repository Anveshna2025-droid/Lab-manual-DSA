# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 7: Arrays 1D (Operations + Shifting Cost)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Understand how insert/delete in arrays causes shifting and impacts complexity.

# Input / Output expectation
# Input: list + position + value. 
# Output: updated list + shift count + complexity statement.

# <=====================CODE STARTS==========================>

class ArrayOperations:
    def __init__(self, capacity=20):
        # Initializing a fixed-size list to simulate a static array
        self.data = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def insert(self, pos, value):
        """
        Inserts a value at a given position and tracks manual shifts.
        """
        if self.size >= self.capacity:
            return "Overflow: Array is full"
        if pos < 0 or pos > self.size:
            return "Invalid position"

        shift_count = 0
        # Shift elements from right to left to create space at 'pos'
        for i in range(self.size, pos, -1):
            self.data[i] = self.data[i-1]
            shift_count += 1
        
        self.data[pos] = value
        self.size += 1
        
        # Complexity Logic
        if pos == self.size - 1:
            complexity = "O(1) - Best Case (Insertion at End)"
        elif pos == 0:
            complexity = "O(n) - Worst Case (Insertion at Start)"
        else:
            complexity = "O(n) - Average Case (Insertion in Middle)"
            
        return shift_count, complexity

    def delete(self, pos):
        """
        Deletes a value at a given position and tracks manual shifts.
        """
        if self.size == 0:
            return "Underflow: Array is empty"
        if pos < 0 or pos >= self.size:
            return "Invalid position"

        shift_count = 0
        # Shift elements from left to right to fill the gap at 'pos'
        for i in range(pos, self.size - 1):
            self.data[i] = self.data[i+1]
            shift_count += 1
        
        self.data[self.size - 1] = None
        self.size -= 1
        
        # Complexity Logic
        if pos == self.size:
            complexity = "O(1) - Best Case (Deletion at End)"
        elif pos == 0:
            complexity = "O(n) - Worst Case (Deletion at Start)"
        else:
            complexity = "O(n) - Average Case (Deletion in Middle)"
            
        return shift_count, complexity

    def display(self):
        return [self.data[i] for i in range(self.size)]

def main():
    # Initialize the array object
    arr_obj = ArrayOperations(capacity=15)
    
    # Pre-loading some elements for the demo
    initial_elements = [10, 20, 30, 40, 50]
    for x in initial_elements:
        arr_obj.insert(arr_obj.size, x)

    while True:
        print("\n" + "="*30)
        print(" ARRAY OPERATIONS MENU ")
        print("="*30)
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Display Array State")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                val = int(input("Enter value to insert: "))
                pos = int(input(f"Enter position (0 to {arr_obj.size}): "))
                result = arr_obj.insert(pos, val)
                
                if isinstance(result, tuple):
                    shifts, comp = result
                    print(f"\n[SUCCESS]")
                    print(f"Updated Array: {arr_obj.display()}")
                    print(f"Shift Count: {shifts}")
                    print(f"Complexity: {comp}")
                else:
                    print(f"\n[ERROR] {result}")
            except ValueError:
                print("\n[ERROR] Please enter valid integers.")

        elif choice == "2":
            try:
                pos = int(input(f"Enter index to delete (0 to {arr_obj.size - 1}): "))
                result = arr_obj.delete(pos)
                
                if isinstance(result, tuple):
                    shifts, comp = result
                    print(f"\n[SUCCESS]")
                    print(f"Updated Array: {arr_obj.display()}")
                    print(f"Shift Count: {shifts}")
                    print(f"Complexity: {comp}")
                else:
                    print(f"\n[ERROR] {result}")
            except ValueError:
                print("\n[ERROR] Please enter valid integers.")

        elif choice == "3":
            print(f"\nCurrent Array: {arr_obj.display()}")
            print(f"Current Size: {arr_obj.size}/{arr_obj.capacity}")

        elif choice == "0":
            print("Terminating the program. Goodbye Anveshna!")
            break
        else:
            print("Invalid Choice! Please select 0-3.")

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>
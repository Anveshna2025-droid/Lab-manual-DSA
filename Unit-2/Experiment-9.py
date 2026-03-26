# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 9: Dynamic Array Simulation (Resize + Pop)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Understand how dynamic arrays grow and why append is amortized O(1).

# Input / Output expectation
# Input: sequence of appends and pops. 
# Output: state print showing resize event(s) (size and capacity).

# <=====================CODE STARTS==========================>

import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0           # Actual number of elements (Size)
        self.capacity = 1    # Total available slots (Capacity)
        self.A = self.make_array(self.capacity)

    def make_array(self, capacity):
        """Returns a new array with a fixed capacity."""
        return (capacity * ctypes.py_object)()

    def append(self, item):
        """Adds an item to the end of the array, resizing if necessary."""
        if self.n == self.capacity:
            print(f"\n[RESIZE EVENT] Capacity {self.capacity} reached. Doubling...")
            self._resize(2 * self.capacity)
        
        self.A[self.n] = item
        self.n += 1
        print(f"Appended {item}: (Size: {self.n}, Capacity: {self.capacity})")

    def _resize(self, new_capacity):
        """Internal method to grow the array capacity."""
        B = self.make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_capacity

    def pop(self):
        """Removes the last element from the array."""
        if self.n == 0:
            print("\n[ERROR] Underflow: Nothing to pop.")
            return None
        
        item = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        print(f"Popped {item}: (Size: {self.n}, Capacity: {self.capacity})")
        return item

    def display(self):
        elements = [self.A[i] for i in range(self.n)]
        return elements

def main():
    print("=== Dynamic Array Simulation (Anveshna) ===")
    arr = DynamicArray()
    
    while True:
        print("\n" + "="*30)
        print(" DYNAMIC ARRAY MENU ")
        print("="*30)
        print("1. Append Element")
        print("2. Pop Element")
        print("3. Display State")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            val = input("Enter value to append: ")
            arr.append(val)

        elif choice == "2":
            arr.pop()

        elif choice == "3":
            print(f"\nElements: {arr.display()}")
            print(f"Current Size: {arr.n}")
            print(f"Current Capacity: {arr.capacity}")

        elif choice == "0":
            print("Experiment 9 complete. See you soon, Sir!")
            break
        else:
            print("Invalid Selection!")

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>
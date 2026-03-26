# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 11: Doubly Linked List (Extended Ops)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Learn bidirectional links and correct pointer updates.

# Input / Output expectation
# Input: target/position. 
# Output: list after each operation.

# <=====================CODE STARTS==========================>

class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Helper to populate the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_after_node(self, target_val, x):
        """Finds target_val and inserts x after it."""
        temp = self.head
        while temp:
            if temp.data == target_val:
                new_node = Node(x)
                new_node.next = temp.next
                new_node.prev = temp
                
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                print(f"Inserted {x} after {target_val}.")
                return
            temp = temp.next
        print(f"Target {target_val} not found.")

    def delete_at_position(self, pos):
        """Deletes node at specific index (0-indexed)."""
        if not self.head:
            print("Underflow: List is empty.")
            return

        temp = self.head

        # Case 1: Delete Head
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"Deleted node at position 0.")
            return

        # Traverse to the position
        for i in range(pos):
            if temp is None:
                print("Position out of bounds.")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds.")
            return

        # Case 2: Delete Middle or Tail
        if temp.next:
            temp.next.prev = temp.prev
        
        if temp.prev:
            temp.prev.next = temp.next
            
        print(f"Deleted node at position {pos} (Value: {temp.data}).")

    def display(self):
        """Displays the list forward and backward to verify prev pointers."""
        if not self.head:
            print("List: Empty")
            return
        
        fwd_elements = []
        temp = self.head
        last = None
        while temp:
            fwd_elements.append(str(temp.data))
            last = temp
            temp = temp.next
        
        print("Forward:  " + " <-> ".join(fwd_elements))

def main():
    print("=== Doubly Linked List Simulation (Anveshna) ===")
    dll = DoublyLinkedList()

    # Initial Data
    for val in [10, 20, 30]:
        dll.insert_at_end(val)

    while True:
        print("\n" + "="*35)
        print(" DLL EXTENDED OPERATIONS MENU ")
        print("="*35)
        print("1. Insert After Value")
        print("2. Delete at Position")
        print("3. Display List")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            target = input("Enter target value to find: ")
            new_val = input("Enter new value to insert: ")
            dll.insert_after_node(target, new_val)
            dll.display()

        elif choice == "2":
            try:
                pos = int(input("Enter position to delete: "))
                dll.delete_at_position(pos)
                dll.display()
            except ValueError:
                print("Please enter a valid numeric position.")

        elif choice == "3":
            dll.display()

        elif choice == "0":
            print("Experiment 11 complete. Well done!")
            break
        else:
            print("Invalid Selection!")

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>
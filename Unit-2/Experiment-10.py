# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 10: Singly Linked List (Core Ops)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement dynamic insertion and deletion without shifting.

# Input / Output expectation
# Input: operation sequence. 
# Output: list after each operation.

# <=====================CODE STARTS==========================>

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """O(1) complexity: No shifting required."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at beginning.")

    def insert_at_end(self, data):
        """O(n) complexity: Must traverse to the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at end.")

    def delete_by_value(self, key):
        """Deletes first occurrence of key. Handles head, middle, and tail."""
        temp = self.head

        # Case 1: Key is at the head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                print(f"Deleted {key} from head.")
                return

        # Case 2: Search for the key (Middle/Tail)
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Case 3: Key not found
        if temp is None:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node
        prev.next = temp.next
        print(f"Deleted {key} from the list.")

    def traverse(self):
        """Displays the list elements."""
        if not self.head:
            print("List is empty.")
            return
        
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("List State: " + " -> ".join(elements) + " -> None")

def main():
    print("=== Singly Linked List Simulation (Anveshna) ===")
    sll = SinglyLinkedList()

    while True:
        print("\n" + "="*35)
        print(" SLL CORE OPERATIONS MENU ")
        print("="*35)
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete by Value")
        print("4. Traverse (Display)")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            val = input("Enter value: ")
            sll.insert_at_beginning(val)
            sll.traverse()

        elif choice == "2":
            val = input("Enter value: ")
            sll.insert_at_end(val)
            sll.traverse()

        elif choice == "3":
            val = input("Enter value to delete: ")
            sll.delete_by_value(val)
            sll.traverse()

        elif choice == "4":
            sll.traverse()

        elif choice == "0":
            print("Experiment 10 complete. Finalizing report...")
            break
        else:
            print("Invalid Selection!")

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>
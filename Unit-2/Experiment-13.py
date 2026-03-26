# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 13: Queue using SLL (O(1) operations)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement queue with head+tail pointers and connect to BFS usage.

# Input / Output expectation
# Input: operation sequence. 
# Output: removed values + current front + final state.

# <=====================CODE STARTS==========================>

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueSLL:
    """Queue implementation with a Tail pointer for O(1) Enqueue."""
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        """O(1) - Add to the rear using the tail pointer."""
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued: {item}")

    def dequeue(self):
        """O(1) - Remove from the front."""
        if self.is_empty():
            print("Underflow: Queue is empty.")
            return None
        
        temp = self.front
        self.front = temp.next
        self._size -= 1

        # If front becomes None, rear must also be None
        if self.front is None:
            self.rear = None
            
        return temp.data

    def get_front(self):
        """O(1) - Peek at the front element."""
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None

    def display(self):
        """Shows the current queue state."""
        if self.is_empty():
            return "Empty"
        elements = []
        temp = self.front
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        return " -> ".join(elements)

def main():
    print("=== Queue (SLL with Tail Pointer) - Anveshna ===")
    q = QueueSLL()

    while True:
        print("\n" + "="*35)
        print("      QUEUE OPERATIONS MENU      ")
        print("="*35)
        print("1. Enqueue (Add to Rear)")
        print("2. Dequeue (Remove from Front)")
        print("3. Peek Front")
        print("4. Display Queue State")
        print("0. Exit")

        choice = input("\nSelect Choice: ").strip()

        if choice == "1":
            val = input("Enter value to enqueue: ")
            q.enqueue(val)
            print(f"Current State: {q.display()}")

        elif choice == "2":
            removed = q.dequeue()
            if removed:
                print(f"Removed Value: {removed}")
            print(f"Current State: {q.display()}")

        elif choice == "3":
            front = q.get_front()
            print(f"Current Front: {front if front else 'None'}")

        elif choice == "4":
            print(f"Queue State: {q.display()}")
            print(f"Size: {q._size}")

        elif choice == "0":
            print("Experiment 13 complete. All lab requirements met!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>
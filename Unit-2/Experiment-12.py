# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 12: Stack using SLL + Parentheses Checker
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Build stack using linked list and apply to bracket validation.

# Input / Output expectation
# Input: strings. 
# Output: True/False for each test string.

# <=====================CODE STARTS==========================>

class Node:
    """A node for the Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None

class StackSLL:
    """Stack implementation using Singly Linked List."""
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """O(1) - Insert at the head of SLL."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """O(1) - Remove from the head of SLL."""
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        """O(1) - View the top element."""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

def is_balanced(expression):
    """Uses StackSLL to validate (), {}, [] in a string."""
    stack = StackSLL()
    # Mapping of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Handle empty string case
    if len(expression) == 0:
        return True

    for char in expression:
        if char in mapping.values():  # If it's an opening bracket
            stack.push(char)
        elif char in mapping.keys():  # If it's a closing bracket
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
                
    return stack.is_empty()

def main():
    print("=== Stack (SLL) & Parentheses Checker (Anveshna) ===")
    
    while True:
        print("\n" + "="*35)
        print(" PARENTHESES CHECKER MENU ")
        print("="*35)
        print("1. Check a String")
        print("2. Run Test Cases")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            s = input("Enter string with brackets: ")
            result = is_balanced(s)
            print(f"Result: {'BALANCED (True)' if result else 'NOT BALANCED (False)'}")

        elif choice == "2":
            test_strings = ["()", "({[]})", "(]", "((", " ", "()[{}]"]
            print("\nAutomated Test Results:")
            for ts in test_strings:
                print(f"String: '{ts}' -> Balanced: {is_balanced(ts)}")

        elif choice == "0":
            print("All Experiments (7-12) Completed. Great job, Anveshna!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>
# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 20
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Build a BST and prove sorted output using inorder traversal.

# Input / Output expectation
# Input: keys to insert + keys to search. 
# Output: inorder list + found/not found status.

#<=====================CODE STARTS==========================>

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

def main():
    print("--- BST CORE OPERATIONS ---")
    keys = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for k in keys:
        root = insert(root, k)
    
    sorted_output = []
    inorder(root, sorted_output)
    
    print(f"Inserted Keys: {keys}")
    print(f"Inorder Traversal (Sorted): {sorted_output}")
    
    target = 40
    found = search(root, target)
    print(f"Search for {target}: {'Found' if found else 'Not Found'}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity (Avg): O(log n) - Height of a balanced tree.")
    print("2. Time Complexity (Worst): O(n) - Occurs in skewed trees.")
    print("3. Property: Inorder traversal of a BST always yields sorted data.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
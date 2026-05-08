# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 21
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Delete nodes correctly while maintaining BST validity for all three cases.

# Input / Output expectation
# Input: delete keys. 
# Output: inorder traversal after each deletion as proof of correctness.

#<=====================CODE STARTS==========================>

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None: return Node(key)
    if key < root.val: root.left = insert(root.left, key)
    else: root.right = insert(root.right, key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None: return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Case 1 & 2: Leaf or Node with one child
        if root.left is None: return root.right
        elif root.right is None: return root.left
        
        # Case 3: Node with two children (Inorder Successor)
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root

def get_inorder(root, res):
    if root:
        get_inorder(root.left, res)
        res.append(root.val)
        get_inorder(root.right, res)

def main():
    print("--- BST DELETION ANALYSIS ---")
    keys = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for k in keys: root = insert(root, k)
    
    for to_delete in [20, 30, 50]:
        root = deleteNode(root, to_delete)
        res = []
        get_inorder(root, res)
        print(f"After deleting {to_delete}: {res}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(h) where h is height of the tree.")
    print("2. Logical Step: Replacing node with inorder successor maintains BST.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
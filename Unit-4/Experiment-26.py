# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 26
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement a Hash Table with Separate Chaining to handle data collisions.

# Input / Output expectation
# Input: Key-value pairs where keys result in the same hash index.
# Output: Display of the hash table buckets showing multiple items in a single chain.

#<=====================CODE STARTS==========================>

class HashTableChaining:
    def __init__(self, size):
        # Initialize the table with empty lists (buckets) for chaining
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        # Basic modulo hash function
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if key already exists in the bucket to update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key is new, append it to the chain at that index
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return "Not Found"

    def display_table(self):
        print("--- HASH TABLE CONTENT (SEPARATE CHAINING) ---")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

def main():
    # Using a small size to force collisions for demonstration
    ht = HashTableChaining(size=5)
    
    # Inserting keys that will collide (10, 15, 20 all mod 5 = 0)
    data = [
        (10, "Apple"), 
        (15, "Banana"), 
        (20, "Cherry"), 
        (12, "Date"), 
        (17, "Elderberry")
    ]
    
    for k, v in data:
        ht.insert(k, v)
    
    ht.display_table()
    
    print("\nRetrieval Checks:")
    print(f"Key 15: {ht.get(15)}")
    print(f"Key 12: {ht.get(12)}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Average Case: O(1) for insertion and lookup.")
    print("2. Worst Case: O(n) - If all keys collide in a single bucket.")
    print("3. Mechanism: Uses Linked Lists (or Python Lists) to store multiple elements at one index.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 28
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement a Bloom Filter to understand probabilistic membership testing.

# Input / Output expectation
# Input: A set of strings to add to the filter and items to check.
# Output: Results showing "Probably Present" or "Definitely Not Present".

#<=====================CODE STARTS==========================>

import math

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hash(self, item, seed):
        # Simple simulated hash function using internal hash and a seed
        return (hash(item) + seed) % self.size

    def add(self, item):
        for i in range(self.hash_count):
            index = self._hash(item, i)
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            index = self._hash(item, i)
            if self.bit_array[index] == 0:
                return "Definitely Not Present"
        return "Probably Present (Possible False Positive)"

def main():
    print("--- BLOOM FILTER ANALYSIS ---")
    # Initialize with 20 bits and 3 hash functions
    bf = BloomFilter(20, 3)
    
    # Adding elements
    items_to_add = ["apple", "banana", "cherry"]
    print(f"Adding items: {items_to_add}")
    for item in items_to_add:
        bf.add(item)
    
    print(f"Current Bit Array: {bf.bit_array}")
    
    # Testing membership
    test_items = ["apple", "banana", "dragonfruit", "grape"]
    print("\nMembership Test Results:")
    for test in test_items:
        print(f"Is '{test}' present? -> {bf.check(test)}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity: O(k) where k is the number of hash functions.")
    print("2. Space Complexity: O(m) where m is the size of the bit array.")
    print("3. Limitation: Can result in false positives but never false negatives.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
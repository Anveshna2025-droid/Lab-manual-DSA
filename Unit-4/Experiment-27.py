# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 27
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Implement a Trie (Prefix Tree) to support efficient prefix-based searching.

# Input / Output expectation
# Input: A set of strings to insert and specific prefixes to search.
# Output: Boolean results indicating if a word or prefix exists in the structure.

#<=====================CODE STARTS==========================>

class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Boolean to mark the end of a complete word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def main():
    print("--- TRIE (PREFIX TREE) ANALYSIS ---")
    my_trie = Trie()
    
    # Inserting a small set of words
    words = ["apple", "app", "apricot", "bat", "ball"]
    print(f"Inserting words: {words}")
    for w in words:
        my_trie.insert(w)
    
    # Testing search and prefix functionality
    test_words = ["apple", "app", "beer"]
    test_prefixes = ["ap", "ba", "ca"]

    print("\nWord Search Results:")
    for tw in test_words:
        print(f"Search '{tw}': {my_trie.search(tw)}")

    print("\nPrefix (starts_with) Results:")
    for tp in test_prefixes:
        print(f"Prefix '{tp}': {my_trie.starts_with(tp)}")

    print("\n" + "="*35)
    print("COMPLEXITY ANALYSIS:")
    print("1. Time Complexity (Insert/Search): O(L) where L is the length of the string.")
    print("2. Space Complexity: O(ALPHABET_SIZE * L * N) in the worst case.")
    print("3. Advantage: Extremely efficient for autocomplete and dictionary lookups.")
    print("="*35)

if __name__ == "__main__":
    main()

#<=====================CODE ENDS============================>
# Proof of Concept Implementation: Core Data Structures in Python
Project Overview
This repository contains the implementation of Phase 2 of the MSCS 634 term project. The objective of this phase is to build a Proof of Concept (PoC) of three core data structures in Python that are vital to search, indexing, and ranking applications. These structures are commonly used in real-time analytics systems, recommendation engines, and search engines.
Implemented Data Structures

Trie
Used for prefix-based search and auto-complete functionality. Supports efficient string insertions and lookups.
Min Heap
Maintains elements in a priority queue where the smallest element is always at the root. Ideal for task scheduling, priority management, and sorting algorithms.
Hash Table
Implements constant-time key-value access with collision handling using separate chaining. Useful for quick lookups and data indexing.

Each data structure is implemented as a standalone Python class with clearly defined methods for insertion, deletion, search, and retrieval. The code follows object-oriented design principles and is modular for future extension.
# Project Structure
.
├── trie.py                 # Implementation of Trie data structure
├── min_heap.py             # Implementation of MinHeap using heapq
├── hash_table.py           # Custom HashTable implementation with separate chaining
├── demo.py                 # Demo script showcasing all three structures
├── README.md               # Project documentation
├── __init__.py         # (Optional) Marks the test directory as a package
├── test_trie.py        # Unit tests for Trie
├── test_min_heap.py    # Unit tests for Min Heap
└── test_hash_table.py  # Unit tests for Hash Table
Running the Demonstration
To see the data structures in action, run the demo script:
bashpython demo.py
Sample output:
TRIE DEMO
Search 'apple': True
Search 'app': True
Starts with 'ap': True
Search 'banana': False

MIN HEAP DEMO
Min element: 3
Removed: 3
New min: 5

HASH TABLE DEMO
Get user1: Alice
Get user1 after delete: None
Running the Unit Tests
The project includes unit tests to ensure correctness and robustness. All test files are located in the tests/ directory.
To run all tests:
bashpython -m unittest discover -s tests
To run a specific test file:
bashpython -m unittest tests.test_trie
Or run a test file directly:
bashpython tests/test_trie.py
Features and Capabilities
Trie

Insert and search for complete words
Check if a prefix exists
Fast traversal using dictionary nodes
Efficient for auto-complete and dictionary lookup applications

Min Heap

Insert integers while maintaining heap properties
Retrieve the minimum element in constant time
Remove the smallest element efficiently
Built using Python's built-in heapq module with a class wrapper

Hash Table

Insert and retrieve key-value pairs
Delete entries by key
Handle collisions using separate chaining
Includes custom hashing logic

Implementation Details
Time Complexities

Trie: Insert/Search: O(m) where m is the length of the word
Min Heap: Insert: O(log n), Extract Min: O(log n), Peek: O(1)
Hash Table: Average case Insert/Search/Delete: O(1), Worst case: O(n)

Space Complexities

Trie: O(ALPHABET_SIZE × N × M) where N is number of words and M is average length
Min Heap: O(n) where n is the number of elements
Hash Table: O(n) where n is the number of key-value pairs

Requirements

Python 3.6 or higher
No external dependencies (uses only built-in Python modules)

Installation

Clone the repository:

bashgit clone <repository-url>
cd core-data-structures-python

No additional installation required - uses only Python standard library

Usage Examples
Trie Example
pythonfrom trie import Trie

trie = Trie()
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))  # True
print(trie.starts_with("ap"))  # True
Min Heap Example
pythonfrom min_heap import MinHeap

heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)

print(heap.get_min())  # 3
print(heap.extract_min())  # 3
Hash Table Example
pythonfrom hash_table import HashTable

ht = HashTable()
ht.put("name", "Alice")
ht.put("age", 25)

print(ht.get("name"))  # Alice
ht.delete("age")
Challenges Encountered

Designing a Trie with both space and time efficiency using nested dictionaries and flags
Abstracting Python's built-in heap operations into a clean object-oriented structure
Implementing a hash table from scratch with bucket-based collision resolution
Maintaining modularity across the codebase for future integration

# Testing
The project includes comprehensive unit tests covering:

Edge cases and boundary conditions
Normal operation scenarios
Error handling and invalid inputs
Performance characteristics

Test coverage includes:

Trie: Word insertion, search, prefix matching, empty trie handling
Min Heap: Heap property maintenance, min extraction, empty heap scenarios
Hash Table: Key-value operations, collision handling, deletion scenarios

Next Steps

Integrate Python's unittest module for automated validation ✅
Run performance benchmarking on large datasets
Add command-line or GUI-based interaction
Extend Trie to track word frequency for better predictions
Enhance Min Heap to support custom objects with comparison logic
Add dynamic resizing to the Hash Table based on load factor
Integrate all data structures into a unified application framework for large-scale data analysis


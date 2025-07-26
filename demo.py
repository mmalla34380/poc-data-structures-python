from trie import Trie
from min_heap import MinHeap
from hash_table import HashTable

def demo_trie():
    print("== TRIE DEMO ==")
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print("Search 'apple':", trie.search("apple"))
    print("Search 'app':", trie.search("app"))
    print("Starts with 'ap':", trie.starts_with("ap"))
    print("Search 'banana':", trie.search("banana"))

def demo_heap():
    print("\n== MIN HEAP DEMO ==")
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    print("Min element:", heap.get_min())
    print("Removed:", heap.remove_min())
    print("New min:", heap.get_min())

def demo_hash_table():
    print("\n== HASH TABLE DEMO ==")
    ht = HashTable()
    ht.insert("user1", "Alice")
    ht.insert("user2", "Bob")
    print("Get user1:", ht.get("user1"))
    ht.delete("user1")
    print("Get user1 after delete:", ht.get("user1"))

if __name__ == "__main__":
    demo_trie()
    demo_heap()
    demo_hash_table()

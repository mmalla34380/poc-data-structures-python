import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.ht = HashTable()

    def test_insert_and_get(self):
        self.ht.insert("user1", "Alice")
        self.ht.insert("user2", "Bob")
        self.assertEqual(self.ht.get("user1"), "Alice")
        self.assertEqual(self.ht.get("user2"), "Bob")

    def test_update_existing_key(self):
        self.ht.insert("user1", "Alice")
        self.ht.insert("user1", "Alicia")
        self.assertEqual(self.ht.get("user1"), "Alicia")

    def test_delete_key(self):
        self.ht.insert("user1", "Alice")
        self.ht.delete("user1")
        self.assertIsNone(self.ht.get("user1"))

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.ht.get("unknown"))

    def test_collision_handling(self):
        # Assuming _hash is basic and small size, collisions may happen
        self.ht.insert("key1", "val1")
        self.ht.insert("key2", "val2")  # could map to same index
        self.assertEqual(self.ht.get("key1"), "val1")
        self.assertEqual(self.ht.get("key2"), "val2")

if __name__ == '__main__':
    unittest.main()

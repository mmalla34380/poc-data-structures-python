import unittest
from min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()

    def test_insert_and_get_min(self):
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.assertEqual(self.heap.get_min(), 3)

    def test_remove_min(self):
        self.heap.insert(10)
        self.heap.insert(1)
        self.heap.insert(7)
        self.assertEqual(self.heap.remove_min(), 1)
        self.assertEqual(self.heap.get_min(), 7)

    def test_empty_heap(self):
        self.assertIsNone(self.heap.get_min())
        self.assertIsNone(self.heap.remove_min())

    def test_insert_duplicates(self):
        self.heap.insert(2)
        self.heap.insert(2)
        self.heap.insert(1)
        self.assertEqual(self.heap.get_min(), 1)

if __name__ == '__main__':
    unittest.main()

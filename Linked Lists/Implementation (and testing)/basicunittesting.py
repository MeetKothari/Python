import unittest

from linkedlist import SinglyLinkedList, Node

class TestSinglyLinkedList(unittest.TestCase):
    
    def test_get_data_from(self):
        # test to see whether the get function works 
        ll = SinglyLinkedList()
        
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        self.assertAlmostEqual(ll.get_data_from(1), 2)
        self.assertAlmostEqual(ll.get_data_from(0), 1)
    
    def test_error(self):
        
        ll = SinglyLinkedList()
        
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        self.assertRaises(TypeError, SinglyLinkedList.get_data_from(), 'orange')

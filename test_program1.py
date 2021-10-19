from program1 import read_sum_write
import unittest
import unittest.mock as um

class TestReadSumWrite(unittest.TestCase):

    def test_nonstring_filename(self):
        print("""It should reject a non-string filename""")
        self.assertRaises(TypeError, lambda: read_sum_write(12))
        
    #mock
    def test_noninteger_input(self):
        print("""It should reject a non-integer input line""")
        with um.patch('builtins.open', um.mock_open(read_data='1\n2.1\n')):
            self.assertRaises(ValueError, lambda: read_sum_write("path.txt"))
    
    #mock
    def test_negative_input(self):
        print("""It should accept negative numbers""")
        with um.patch('builtins.open', um.mock_open(read_data='-1\n2\n-3\n')):
            self.assertEqual(read_sum_write("path.txt"), -2)

    #mock #dummy
    def test_return_type(self):    
        print("""It should return an integer""")
        with um.patch('builtins.open', um.mock_open(read_data='')):
            self.assertEqual(type(read_sum_write("path.txt")), int)

    #mock
    def test_write(self):    
        print("""It should write to a file""")
        m = um.mock_open(read_data='1\n2\n')
        with um.patch('builtins.open', m):
            read_sum_write("path.txt")
            handle = m()
            handle.write.assert_called_once()
    
    #mock
    def test_sum(self):
        print("""It should sum the numbers and return the correct result""")
        with um.patch('builtins.open', um.mock_open(read_data='1\n2\n3\n')):
            self.assertEqual(read_sum_write("path.txt"), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
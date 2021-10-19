from program2 import *
import unittest
import unittest.mock as um
import sqlite3
import time

class dbFake:
    def __init__(self):
        self.dict = {}

class TestAccountingDBProgram(unittest.TestCase):

    #mock #dummy
    def test_insert_customer_execute(self):
        print("""insert_customer should execute a sql command for insert_customer""")
        with um.patch('program2.sqlite3') as mock_sql:
            insert_customer(time.time_ns() % 1000000, "coke", 4)
            mock_sql.connect().commit.assert_called_once()
            
    #dummy
    def test_insert_customer_nonstring_name(self):
        print("""insert_customer should reject non-string customer names""")
        self.assertRaises(TypeError, lambda: insert_customer(999, 999, 4))

    #dummy
    def test_insert_customer_noninteger_goods(self):
        print("""insert_customer should reject non-integer customer tot_goods""")
        self.assertRaises(TypeError, lambda: insert_customer(995, "coke", "pepsi"))
    
    #dummy
    def test_insert_customer_noninteger_id(self):
        print("""insert_customer should reject non-integer customer ids""")
        self.assertRaises(TypeError, lambda: insert_customer("orange", "coke", 4))
    
    #dummy    
    def test_insert_customer_negative_goods(self):
        print("""insert_customer should reject negative customer tot_goods""")
        self.assertRaises(ValueError, lambda: insert_customer(995, "coke", -100))


    #mock #dummy
    def test_insert_order_execute(self):
        print("""insert_order should execute a sql command""")
        with um.patch('program2.sqlite3') as mock_sql:
            insert_order(time.time_ns() % 1000000, 4)
            mock_sql.connect().commit.assert_called_once()
    
    #dummy
    def test_insert_order_noninteger_goods(self):
        print("""insert_order should reject non-integer goods""")
        self.assertRaises(TypeError, lambda: insert_order(995, "sprite"))
    
    #dummy
    def test_insert_order_noninteger_id(self):
        print("""insert_order should reject non-integer customer ids""")
        self.assertRaises(TypeError, lambda: insert_order("fanta",10))
        
    #dummy
    def test_insert_order_negative_goods(self):
        print("""insert_order should reject negative goods""")
        self.assertRaises(ValueError, lambda: insert_order(995, -100))


    #mock
    def test_retrieve_customers_execute(self):
        print("""retrieve_customers should execute a sql command""")
        with um.patch('program2.sqlite3') as mock_sql:
            retrieve_customers()
            mock_sql.connect().commit.assert_called_once()

    #stub #mock
    def test_retrieve_customers_execute(self):
        print("""retrieve_customers should return""")
        with um.patch('program2.sqlite3') as mock_sql:
            mock_sql.connect().cursor().fetchall.return_value = [(123, 'coke', 5), (128, 'poke', 4), (151300, 'coke', 4)]
            value = retrieve_customers()
            self.assertEqual(type(value), list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
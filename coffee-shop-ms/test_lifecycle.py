import unittest

class TestLifeCycle (unittest.TestCase):
    def setUp(self):
       self.data= {"product":[]}
    def tearDown(self):
        print("test finished")
    def test_add_product(self):
        product = "latte"
        self.data["product"].append(product)
        self.assertEqual(len(self.data["product"]), 1)
    def test_empty_products(self):
        self.assertEqual(len(self.data["product"]), 0)
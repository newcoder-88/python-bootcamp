import unittest
from orders import validate_quantity, validate_order


data = {
    "Products": [
        {"id": 1, "name": "Latte", "price": 18},
        {"id": 2, "name": "Espresso", "price": 12}
    ]
}


class TestValidation(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(validate_quantity(5), 5) 

    def test_invalid_quantity(self):
        self.assertRaises(ValueError, validate_quantity, -3)

    def test_invalid_quantity_message(self):
        with self.assertRaises(ValueError) as context:
            validate_quantity(0)
        self.assertEqual(str(context.exception),"Quantity must be greater than zero" )

    def test_valid_order(self):
        result= validate_order(data,2,3)
        self.assertEqual(result["quantity"], 3)
        self.assertEqual(result["product"]["name"], "Espresso")

    def test_invalid_order_product(self):
        with self.assertRaises(ValueError):
            validate_order(data, 999, 3)

    def test_invalid_order_quantity(self):
        with self.assertRaises(ValueError):
            validate_order(data, 2, -3)

    def test_invalid_order_product_message(self):
        with self.assertRaises(ValueError) as context:
            validate_order(data,999,3)
        self.assertEqual(str(context.exception), "product not found")
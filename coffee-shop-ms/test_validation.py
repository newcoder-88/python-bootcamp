import unittest
from unittest.mock import patch
from orders import validate_quantity, validate_order

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.data = {
            "Products": [
                {"id": 1, "name": "Latte", "price": 18},
                {"id": 2, "name": "Espresso", "price": 12}
            ]
        }

    def test_valid_quantity(self):
        self.assertEqual(validate_quantity(5), 5) 

    def test_invalid_quantity(self):
        self.assertRaises(ValueError, validate_quantity, -3)

    def test_invalid_quantity_message(self):
        with self.assertRaises(ValueError) as context:
            validate_quantity(0)
        self.assertEqual(str(context.exception),"Quantity must be greater than zero" )

    def test_valid_order(self):
        result= validate_order(self.data,2,3)
        self.assertEqual(result["quantity"], 3)
        self.assertEqual(result["product"]["name"], "Espresso")

    def test_invalid_order_product(self):
        with self.assertRaises(ValueError):
            validate_order(self.data, 999, 3)

    def test_invalid_order_quantity(self):
        with self.assertRaises(ValueError):
            validate_order(self.data, 2, -3)

    def test_invalid_order_product_message(self):
        with self.assertRaises(ValueError) as context:
            validate_order(self.data,999,3)
        self.assertEqual(str(context.exception), "product not found")

    def test_quantity_boundary(self):
        with self.assertRaises(ValueError) as context:
            validate_quantity(0)
        self.assertEqual(str(context.exception),"Quantity must be greater than zero")
        self.assertEqual(validate_quantity(1), 1)
        self.assertRaises(ValueError,validate_quantity,-1 )


    def test_validate_order_with_mock(self):
        with patch("orders.get_valid_product") as mock_product:
            mock_product.return_value = {"id": 1, "name": "Latte", "price": 18}
            result = validate_order(self.data, 1, 2)
            expected = {"product":mock_product.return_value , "quantity": 2}
            self.assertEqual(result, expected)
            mock_product.assert_called_once_with(self.data, 1)

    def test_validate_order_mock_error(self):
        with patch("orders.get_valid_product") as mock_product:
            mock_product.side_effect = ValueError("product not found")
            with self.assertRaises(ValueError) as context:
                validate_order(self.data, 99, 2)
            self.assertEqual(str(context.exception), "product not found")
            mock_product.assert_called_once_with(self.data, 99)

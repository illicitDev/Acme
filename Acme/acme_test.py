"""Test Product and Report Modules"""
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test stealability method"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

    def test_explode(self):
        """Test explode method"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Test default number of products in generate products method"""
        pord_list = generate_products()
        self.assertEqual(len(pord_list), 30)

    def test_legal_names(self):
        """Test is name assigned is legal"""
        prod_list = generate_products()
        for product in prod_list:
            names = product.name.split()
            
            self.assertIn(names[0], ADJECTIVES)
            self.assertIn(names[1], NOUNS)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, Mock
from api_client import fetch_products_by_brand
from product import Product
from utils import check_python_version

class TestBeautyApp(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_products_by_brand_success(self, mock_get):
        # Mock da resposta da API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Product 1", "price": "5.00", "description": "Desc 1", "product_link": "link1", "brand": "nyx"},
            {"name": "Product 2", "price": "10.00", "description": "Desc 2", "product_link": "link2", "brand": "nyx"}
        ]
        mock_get.return_value = mock_response

        # Testa a função
        products = fetch_products_by_brand("nyx")
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0]["name"], "Product 1")
        self.assertEqual(products[1]["price"], "10.00")

    @patch('requests.get')
    def test_fetch_products_by_brand_failure(self, mock_get):
        # Mock de uma falha na requisição
        mock_get.side_effect = Exception("Erro na requisição")

        # Testa a função
        products = fetch_products_by_brand("marca_inexistente")
        self.assertIsNone(products)

    def test_product_class(self):
        # Testa a criação de um objeto Product
        product = Product("Product 1", "5.00", "Desc 1", "link1", "nyx")
        self.assertEqual(product.name, "Product 1")
        self.assertEqual(product.price, "5.00")
        self.assertEqual(product.brand, "nyx")

    def test_check_python_version_valid(self):
        # Testa a função check_python_version com uma versão válida
        with patch('sys.version_info', (3, 9)):
            try:
                check_python_version()
            except RuntimeError:
                self.fail("check_python_version() levantou RuntimeError com uma versão válida.")

    def test_check_python_version_invalid(self):
        # Testa a função check_python_version com uma versão inválida
        with patch('sys.version_info', (3, 5)):
            with self.assertRaises(RuntimeError):
                check_python_version()

    def test_filter_products_by_price(self):
        # Testa o filtro por preço máximo
        products_data = [
            {"name": "Product 1", "price": "5.00", "description": "Desc 1", "product_link": "link1", "brand": "nyx"},
            {"name": "Product 2", "price": "10.00", "description": "Desc 2", "product_link": "link2", "brand": "nyx"}
        ]
        max_price = 8.00

        # Filtra os produtos
        filtered_products = [
            product for product in products_data
            if product.get('price', 'N/A') != 'N/A' and float(product['price']) <= max_price
        ]

        self.assertEqual(len(filtered_products), 1)
        self.assertEqual(filtered_products[0]["name"], "Product 1")

if __name__ == "__main__":
    unittest.main()
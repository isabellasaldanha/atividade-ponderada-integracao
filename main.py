import logging
from api_client import fetch_products_by_brand
from product import Product
from utils import setup_logging, check_python_version

def main():
    setup_logging()
    logging.info("Iniciando a aplicação de busca de produtos de beleza.")

    try:
        check_python_version()

        brand = input("Digite a marca do produto que deseja buscar (ex: maybelline): ").strip()
        if not brand:
            print("Marca não fornecida. Por favor, tente novamente.")
            return

        # Regra de negócio que filtra os produtos por um preço máximo
        try:
            max_price = float(input("Digite o preço máximo que deseja pagar (ex: 10.00): ").strip())
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")
            return

        products_data = fetch_products_by_brand(brand)
        if products_data:

            filtered_products = [
                product for product in products_data
                if product.get('price', 'N/A') != 'N/A' and float(product['price']) <= max_price
            ]

            if filtered_products:
                products = [Product(
                    name=product.get('name', 'N/A'),
                    price=product.get('price', 'N/A'),
                    description=product.get('description', 'N/A'),
                    product_link=product.get('product_link', 'N/A'),
                    brand=product.get('brand', 'N/A')
                ) for product in filtered_products]

                print(f"\nProdutos encontrados da marca {brand} com preço até ${max_price:.2f}:")
                for product in products:
                    print(product)  
            else:
                print(f"Nenhum produto encontrado da marca {brand} com preço até ${max_price:.2f}.")
        else:
            print(f"Nenhum produto encontrado para a marca {brand}.")
    except Exception as e:
        logging.error(f"Erro na execução do programa: {e}", exc_info=True)
        print("Ocorreu um erro no programa. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
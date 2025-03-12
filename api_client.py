import requests
import logging
import time
from urllib.parse import urlparse

API_URL = "http://makeup-api.herokuapp.com/api/v1/products.json"

def fetch_products_by_brand(brand):
    try:
        # Verifica o protocolo da URL da API
        protocol = urlparse(API_URL).scheme
        if protocol not in ["http", "https"]:
            logging.warning(f"Protocolo não suportado: {protocol}. Utilize HTTP ou HTTPS.")

        # Medição do tempo de resposta
        start_time = time.time()

        # Faz a requisição à API
        params = {'brand': brand}
        response = requests.get(API_URL, params=params, timeout=10)  # Timeout de 10 segundos
        response.raise_for_status()  # Lança uma exceção para respostas não bem-sucedidas

        # Calcula o tempo de resposta
        end_time = time.time()
        response_time = end_time - start_time
        logging.info(f"Requisição à API concluída em {response_time:.2f} segundos.")

        products = response.json()
        logging.info(f"Produtos da marca {brand} buscados com sucesso.")
        return products

    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição à API: {e}")
        return None
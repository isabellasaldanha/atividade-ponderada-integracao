## BDD e Engenharia de Integração - Ponderada 3

### a) Estrutura de integração

#### **Camadas do projeto**
O projeto é dividido em três camadas principais:

1. **Interface do usuário (UI)**:
   - O usuário interage com o sistema por meio de um prompt de comando, onde insere a marca do produto de beleza que deseja buscar e o preço máximo que está disposto a pagar.

2. **Lógica de negócio**:
   - Responsável por processar a entrada do usuário, fazer a requisição à API externa, filtrar os produtos com base no preço máximo e tratar os dados retornados.

3. **API externa**:
   - Utiliza a **Makeup API** (https://makeup-api.herokuapp.com/) para buscar informações sobre produtos de beleza.


#### **Módulos**
O projeto é organizado em quatro módulos principais:

1. **`main.py`**:
   - Arquivo principal que inicia a aplicação, gerencia a interação com o usuário e aplica a regra de negócio (filtro por preço máximo).

2. **`api_client.py`**:
   - Responsável por fazer as requisições à API externa e tratar as respostas.

3. **`product.py`**:
   - Define a estrutura de um produto de beleza, encapsulando os atributos como nome, preço, descrição, link e marca.

4. **`utils.py`**:
   - Contém funções utilitárias, como configuração de logging e verificação da versão do Python.

#### **Componentes**
Os principais componentes do projeto são:

1. **Requisições HTTP**:
   - Utiliza a biblioteca `requests` para fazer requisições à API.

2. **Tratamento de exceções**:
   - Captura e registra erros de rede, respostas inválidas da API e problemas no código.

3. **Logging**:
   - Registra eventos importantes, como sucesso ou falha nas requisições, em um arquivo de log (`beauty_app.log`).

4. **Filtro por preço máximo**:
   - Implementa a regra de negócio que filtra os produtos com base no preço máximo informado pelo usuário.


#### **Serviços**
O projeto utiliza os seguintes serviços:

1. **Makeup API**:
   - Serviço externo que fornece dados sobre produtos de beleza, como nome, preço, descrição e link.


#### **Processos**
O fluxo de execução do projeto segue os seguintes passos:

1. O usuário insere a marca do produto que deseja buscar.
2. O usuário insere o preço máximo que está disposto a pagar.
3. O sistema faz uma requisição à Makeup API, passando a marca como parâmetro.
4. A API retorna uma lista de produtos da marca especificada.
5. O sistema filtra os produtos com base no preço máximo informado.
6. O sistema exibe os produtos filtrados, incluindo nome, preço, descrição e link.
7. Se ocorrer algum erro, o sistema exibe uma mensagem de erro e registra o problema no log.


### b) Controle de qualidade de integração

O controle de qualidade de integração inclui medição de tempos, verificação de protocolos, controle de versões e tratamento de exceções.

#### **Tempos**
- O tempo de resposta da API é medido usando `time.time()` antes e depois de cada requisição.
- O tempo é registrado no log para monitoramento.

#### **Protocolos**
- O protocolo da URL da API é verificado usando `urlparse`.
- Se o protocolo não for HTTP ou HTTPS, um aviso é registrado no log.

#### **Versões**
- A versão do Python é verificada no início do programa.
- Se a versão for inferior à 3.6, o programa é interrompido.
- A versão da API (v1) está codificada na URL (`http://makeup-api.herokuapp.com/api/v1/products.json`).

#### **Tratamento de exceções**
- Erros de rede, como falhas na conexão, são tratados com `requests.exceptions.RequestException`.
- Erros na resposta da API são tratados com `response.raise_for_status()`.
- Erros no código são capturados com um `try-except` genérico no `main.py`.

### c) Testes unitários

Os testes unitários garantem que cada componente do projeto funcione corretamente de forma isolada. Eles estão organizados na pasta `tests` e cobrem as seguintes funcionalidades:

1. **Requisição à API**:
   - Verifica se a API retorna dados válidos para uma marca existente.
   - Verifica o tratamento de erros para uma marca inexistente.

2. **Filtro por preço máximo**:
   - Verifica se o filtro funciona corretamente para diferentes valores de preço máximo.

3. **Classe `Product`**:
   - Verifica se a classe `Product` está sendo instanciada corretamente.

4. **Funções utilitárias**:
   - Verifica a função `check_python_version`.

#### **Exemplo de teste**

##### Teste de filtro por preço máximo
```python
def test_filter_products_by_price(self):
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
```

#### **Como executar os testes**

1. Navegue até a pasta raiz do projeto (`beauty_project`):
   ```bash
   cd caminho/para/beauty_project
   ```

2. Execute os testes:
   ```bash
   python -m unittest tests/test_beauty_app.py
   ```

3. **Resultado esperado**:
   - Se tudo estiver correto, você verá uma saída como:
     ```
     .....
     ----------------------------------------------------------------------
     Ran 5 tests in 0.002s

     OK
     ```


## BDD e Engenharia de Integração - Ponderada 3

### a) Estrutura de Integração

#### **Camadas do Projeto**
O projeto é dividido em três camadas principais:

1. **Interface do Usuário (UI)**:
   - O usuário interage com o sistema por meio de um prompt de comando, onde insere a marca do produto de beleza que deseja buscar e o preço máximo que está disposto a pagar.

2. **Lógica de Negócio**:
   - Responsável por processar a entrada do usuário, fazer a requisição à API externa, filtrar os produtos com base no preço máximo e tratar os dados retornados.

3. **API Externa**:
   - Utiliza a **Makeup API** (https://makeup-api.herokuapp.com/) para buscar informações sobre produtos de beleza.

---

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

---

#### **Componentes**
Os principais componentes do projeto são:

1. **Requisições HTTP**:
   - Utiliza a biblioteca `requests` para fazer requisições à API.

2. **Tratamento de Exceções**:
   - Captura e registra erros de rede, respostas inválidas da API e problemas no código.

3. **Logging**:
   - Registra eventos importantes, como sucesso ou falha nas requisições, em um arquivo de log (`beauty_app.log`).

4. **Filtro por Preço Máximo**:
   - Implementa a regra de negócio que filtra os produtos com base no preço máximo informado pelo usuário.

---

#### **Serviços**
O projeto utiliza os seguintes serviços:

1. **Makeup API**:
   - Serviço externo que fornece dados sobre produtos de beleza, como nome, preço, descrição e link.

---

#### **Hardware/Software**
- **Hardware**:
  - Qualquer computador ou servidor capaz de executar Python.
  
- **Software**:
  - **Python 3.6 ou superior**.
  - Bibliotecas: `requests`, `logging`.

---

#### **Processos**
O fluxo de execução do projeto segue os seguintes passos:

1. O usuário insere a marca do produto que deseja buscar.
2. O usuário insere o preço máximo que está disposto a pagar.
3. O sistema faz uma requisição à Makeup API, passando a marca como parâmetro.
4. A API retorna uma lista de produtos da marca especificada.
5. O sistema filtra os produtos com base no preço máximo informado.
6. O sistema exibe os produtos filtrados, incluindo nome, preço, descrição e link.
7. Se ocorrer algum erro, o sistema exibe uma mensagem de erro e registra o problema no log.

---

### b) Controle de Qualidade de Integração

O controle de qualidade de integração inclui medição de tempos, verificação de protocolos, controle de versões e tratamento de exceções.

---

#### **Tempos**
- O tempo de resposta da API é medido usando `time.time()` antes e depois de cada requisição.
- O tempo é registrado no log para monitoramento.
- Exemplo de log:
  ```
  2023-10-10 12:00:00,000 - INFO - Requisição à API concluída em 0.50 segundos.
  ```

---

#### **Protocolos**
- O protocolo da URL da API é verificado usando `urlparse`.
- Se o protocolo não for HTTP ou HTTPS, um aviso é registrado no log.
- Exemplo de log:
  ```
  2023-10-10 12:00:00,000 - WARNING - Protocolo não suportado: ftp. Utilize HTTP ou HTTPS.
  ```

---

#### **Versões**
- A versão do Python é verificada no início do programa.
- Se a versão for inferior à 3.6, o programa é interrompido.
- A versão da API (v1) está codificada na URL (`http://makeup-api.herokuapp.com/api/v1/products.json`).
- Exemplo de log:
  ```
  2023-10-10 12:00:00,000 - INFO - Versão do Python: 3.9.7
  ```

---

#### **Tratamento de Exceções**
- Erros de rede, como falhas na conexão, são tratados com `requests.exceptions.RequestException`.
- Erros na resposta da API são tratados com `response.raise_for_status()`.
- Erros no código são capturados com um `try-except` genérico no `main.py`.
- Exemplo de log:
  ```
  2023-10-10 12:00:00,000 - ERROR - Erro na requisição à API: HTTPConnectionPool(host='makeup-api.herokuapp.com', port=80): Max retries exceeded...
  ```

---

### Regra de Negócio: Filtro por Preço Máximo

#### **Descrição**
- O sistema filtra os produtos da marca informada, exibindo apenas aqueles com preço menor ou igual ao valor máximo informado pelo usuário.

#### **Implementação**
1. O usuário informa o preço máximo.
2. O sistema converte o preço dos produtos para `float` e compara com o valor máximo.
3. Apenas os produtos que atendem ao critério são exibidos.

#### **Exceções**
- Se o usuário inserir um valor inválido (não numérico), o sistema exibe uma mensagem de erro e interrompe a busca.

---

### Exemplo de Fluxo de Integração

1. **Entrada do Usuário**:
   - O usuário digita a marca do produto que deseja buscar (ex: "nyx").
   - O usuário digita o preço máximo que está disposto a pagar (ex: "8.00").

2. **Requisição à API**:
   - O sistema faz uma requisição à Makeup API, passando a marca como parâmetro.

3. **Filtragem dos Produtos**:
   - O sistema filtra os produtos da marca informada, exibindo apenas aqueles com preço menor ou igual ao valor máximo.

4. **Exibição dos Resultados**:
   - Os produtos filtrados são exibidos com nome, preço, descrição e link.

5. **Tratamento de Erros**:
   - Se ocorrer algum erro durante a requisição, o sistema exibe uma mensagem de erro e registra o erro no log.

---

### Exemplo de Saída

#### Entrada:
```
Digite a marca do produto que deseja buscar (ex: maybelline): nyx
Digite o preço máximo que deseja pagar (ex: 10.00): 8.00
```

#### Saída:
```
Produtos encontrados da marca nyx com preço até $8.00:
Produto: NYX Professional Makeup Soft Matte Lip Cream
Marca: nyx
Preço: $6.00
Descrição: NYX Professional Makeup Soft Matte Lip Cream...
Link: https://example.com/product1
----------------------------------------
Produto: NYX Professional Makeup Butter Gloss
Marca: nyx
Preço: $5.00
Descrição: NYX Professional Makeup Butter Gloss...
Link: https://example.com/product2
----------------------------------------
```

Se não houver produtos dentro do preço máximo, a saída será:
```
Nenhum produto encontrado da marca nyx com preço até $8.00.
```

---

### Conclusão

Este projeto demonstra como integrar uma aplicação Python com uma API externa, utilizando boas práticas de controle de qualidade de integração e implementando uma regra de negócio (filtro por preço máximo). A documentação detalha a estrutura do projeto, os componentes utilizados, o controle de qualidade e a regra de negócio implementada.


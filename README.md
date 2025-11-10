# EDA de uma tech store 

## Descrição
Este projeto realiza uma análise exploratória de dados de vendas utilizando Python e Pandas. O script processa um arquivo CSV contendo informações sobre vendas de produtos e gera insights relevantes para o negócio.

## Requisitos
- Python 3.x
- Pandas
- matplotlib

### Instalação das dependências
```bash
pip install pandas
pip install matplotlib
```

## Estrutura do Dataset
O arquivo `vendas.csv` contém as seguintes colunas:
- `produto`: Nome do produto
- `categoria`: Categoria do produto
- `quantidade`: Quantidade vendida
- `preco_unitario`: Preço unitário do produto
- `regiao`: Região onde ocorreu a venda
- `data`: Data da compra
- `cliente`: Cliente que fez a compra

## Funcionalidades

### 1. Visualização Inicial
Exibe as 5 primeiras linhas do dataset para inspeção rápida dos dados.

### 2. Total de Registros
Calcula e exibe o número total de linhas (vendas) no dataset.

### 3. Receita Total
Calcula a receita total multiplicando a quantidade pelo preço unitário de cada venda e somando todos os valores.

### 4. Filtro por Categoria
Filtra e exibe apenas os produtos da categoria "Eletrônicos".

### 5. Produto Mais Vendido
Identifica qual produto teve a maior quantidade de vendas através de agrupamento e ordenação.

### 6. Região com Maior Faturamento
Determina qual região gerou o maior valor total em vendas.

## Como Executar

1. Certifique-se de que o arquivo `vendas.csv` está no mesmo diretório do script
2. Execute o script:
```bash
python analyses.py
```
3. Se quiser ver os gráficos disponiveis, execute:
```bash
python graphs.py
```

## Resultados Esperados

O script irá imprimir no console:
- As 5 primeiras linhas do dataset
- Total de linhas processadas
- Receita total gerada
- Listagem de produtos eletrônicos
- Produto com maior quantidade vendida
- Região com maior faturamento

import pandas as pd

df = pd.read_csv('vendas.csv')

# 5 primeiras linhas do dataset
top_5 = df.head()
print(top_5)

# Total de linhas
total_linhas = df.shape[0]
print(f"Total de linhas: {total_linhas}")

# Receita total
df["valor_pedido"] = df["quantidade"] * df["preco_unitario"]
receita_total = df["valor_pedido"].sum()
print(receita_total)

# Filtro -> Categoria = "Eletrônicos"

df_eletronicos = df[df["categoria"] == "Eletrônicos"]
print(df_eletronicos)

# Produto mais vendido

df_produtos_quantidade = df.groupby("produto")["quantidade"].sum()
df_produtos_quantidade.sort_values(inplace=True)
produto_mais_vendido = df_produtos_quantidade.tail(1)
print(produto_mais_vendido)

# Região com mais vendas
df_regiao = df.groupby("regiao")["valor_pedido"].sum()
df_regiao.sort_values(inplace=True)
regiao_mais_vendas = df_regiao.tail(1)
print(regiao_mais_vendas)


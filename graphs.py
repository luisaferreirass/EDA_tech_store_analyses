import pandas as pd
import matplotlib.pyplot as plt
from analyses import df

# Gráfico Receita por Categoria
receita_categoria  = df.groupby("categoria")["valor_pedido"].sum()
receita_categoria.plot(kind='bar', color='skyblue')

plt.title('Receita por categoria')
plt.xlabel('Categoria')
plt.ylabel('Receita')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico Evolução das Vendas por Mês
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month

vendas_mes = df.groupby("mes").size()
vendas_mes.plot(kind='line', marker='o', color='green')
plt.title('Evolução das Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.grid(True)
plt.tight_layout()
plt.show()

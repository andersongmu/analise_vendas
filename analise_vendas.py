import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'produto': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C', 'Produto A'],
    'valor_venda': [100, 150, 120, 80, 200, 130, 110],
    'data': ['2023-01-01', '2023-01-05', '2023-02-10', '2023-02-15', '2023-03-20', '2023-03-25', '2023-04-02']
}
df = pd.DataFrame(dados)

df['data'] = pd.to_datetime(df['data'])

produtos_mais_vendidos = df['produto'].value_counts().head(5)
print("Produtos mais vendidos:")
print(produtos_mais_vendidos)

df['mes'] = df['data'].dt.month
vendas_por_mes = df.groupby('mes')['valor_venda'].sum()
print("Total de vendas por mês:")
print(vendas_por_mes)

vendas_por_mes.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.title('Vendas Mensais')
plt.xticks(rotation=0)
plt.show()

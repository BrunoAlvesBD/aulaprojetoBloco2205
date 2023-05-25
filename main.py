import pandas as pd
import matplotlib.pyplot as plt

# lendo arquivo com base de dados 
arquivo = "casos_resumido.csv"

# importando
bd = pd.read_csv(arquivo, sep=",")



# cabeçalho:
print(f"Original:\{bd.head(0)}")


# normalização de dados
bd['confirmed_norm'] = bd['confirmed']/bd['confirmed'].abs().max()

bd['deaths_norm'] = bd['deaths']/bd['deaths'].abs().max()

# cabeçalho com nova estrutuura
print(f"Nova estrutura:\{bd.head(0)}")

# imprimir primeira linha
# print(bd.head(0))

print(f"total de casos: {bd['confirmed'][1]}\
\nTotal de mortes: {bd['deaths'][1]}")

# ---------------------
print(f"Máximo de casos confirmados: {bd['confirmed'].max()}\
\nMádia de casos: {bd['deaths'].mean()}")

# gráficos com matplotlib 
bd['confirmed_norm'].plot(label='casos',color='green')

bd['deaths_norm'].plot(label='morte',color='red')

plt.title('Número de casos donfirmados')
plt.xlabel('Dias')
plt.ylabel('Quantidade')
plt.show()
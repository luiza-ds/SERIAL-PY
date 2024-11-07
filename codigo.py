import pandas as pd

df=pd.read_csv("/content/dados 1.txt",sep=";")

df.shape #saber as linhas e colunas

df.info() #me da informações do conjunto, como o str, se é int, float

df.describe()  #me da medidas estatisticas

df.groupby('Genero')['Idade', 'AnoDaMorte'].describe()

df.head(5) #vejo as 5 primeiras linhas do meu conjunto

df.columns #me mostrando as as variáveis do meu df (colunas)

display(df) #dessa forma, eu consigo ver o meu df de forma mais bonitinha, diferente do print

df['Genero'] #buscando somente a coluna genero

df.Idade.mean() #calculou a media somente da coluna idade

df.Idade.mean(), df.AnoDaMorte.mean() #puxo somente as medias das variáveis que eu quero

#puxando em uma lista a media da variável Idade e o seu desvio padrão
df.Idade.mean(), df.Idade.std()

#no meu df, esta tudo certo
#entrei na minha variavel ano da morte, transformei tudo para numerico, e caso houvesse algo contrario de numerico, por NaN
df["AnoDaMorte"] = pd.to_numeric(df["AnoDaMorte"], errors="coerce")
print(df.info)

#iremos deletar colunas vazias
#axis = 1 (coluna), axis = 0 (linhas)
df = df.dropna(axis = 1, how="all")

#Estou agrupando por genero e me devolvendo as medidas descritivas com relação a idade
df.groupby('Genero')['Idade'].describe()

df.groupby('Genero')['LocalDaMorte'].describe()

#Estou agora, agrupando por genero e contando o local da morte por sexo das vítimas

df.groupby('Genero')['LocalDaMorte'].value_counts()

df['AnoDaMorte'].value_counts()

df.groupby(['Genero', 'LocalDaMorte'])['AnoDaMorte'].value_counts()

#aqui estou armazenando em "new" o meu agrupamento de dados com coluna genero,localdamorte, anodamorte fazendo em cima da media das idades
#ou seja, na combinação de um tal genero com tal local de morte e em um ano ele me dara a media de idade

new = df.groupby(['Genero','LocalDaMorte', 'AnoDaMorte'])['Idade'].mean()
print(new)

type(new)
#retorna a classe

PARA PLOTAR GRÁFICOS:

NOME DO DF.PLOT(kind='bar', xlabel "", ylabel = "")

df.boxplot(column = 'Idade', by = 'Genero')

df.plot(kind = 'scatter', x = 'AnoDaMorte', y = 'Idade')

df.plot(kind = 'hist', y = 'Idade')

import plotly.express as px

px.histogram(df, x = 'Idade')

px.histogram(df, x = 'Genero')

hist = px.histogram(df, x = 'LocalDaMorte')
hist.show()

box = px.box(df, x = 'Genero', y = 'Idade')
box.show()

#ano da morte X genero

mortes_por_ano_genero = df.groupby(['AnoDaMorte', 'Genero']).size().unstack()
mortes_por_ano_genero.plot(kind = 'bar')

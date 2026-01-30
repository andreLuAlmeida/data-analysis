import pandas as pd
import seaborn as sns
import statistics as sts

#importar dados
dataset = pd.read_csv('tempo.csv', sep=';')

#visualizar dados
print(dataset.head())

#tamanho
print(dataset.shape)

#explorar dados categoricos
print(dataset.groupby(['Aparencia']).size())

#explorar colunas numericas
print(dataset['Temperatura'].describe())

#umidade
print()
print(dataset['Umidade'].describe())

#jogar
print()
print(dataset.groupby(['Jogar']).size())

#contamos valores NaN
print()
print(dataset.isnull().sum())

#tratar valores NaN umidade
mediana_umidade = sts.median(dataset['Umidade'].dropna())
dataset['Umidade'] = dataset['Umidade'].fillna(mediana_umidade)

#verificar se ainda ha valores NaN
print()
print(dataset['Umidade'].isnull().sum())

#tratar valores NaN vento
moda_vento = dataset['Vento'].mode()[0]
dataset['Vento'] = dataset['Vento'].fillna(moda_vento)

#verificar se ainda ha valores NaN
print()
print(dataset['Vento'].isnull().sum())

#padronização de acordo com o dominio
valores_validos = ['sol', 'chuva', 'nublado']

moda_aparencia = (
    dataset.loc[
        dataset['Aparencia'].isin(valores_validos),
        'Aparencia'
    ]
    .mode()[0]
)

dataset.loc[
    ~dataset['Aparencia'].isin(valores_validos),
    'Aparencia'
] = moda_aparencia
#visualizar dados apos tratamento
print()
print(dataset.groupby(['Aparencia']).size())

#temperatura fora do padrao
print()
print(dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)])
temperadura_mediana = int(sts.median(dataset['Temperatura']))
dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130), 'Temperatura'] = temperadura_mediana

#verficar dados apos tratamento
print()
print(dataset.loc[(dataset['Temperatura'] < -130) | (dataset['Temperatura'] > 130)])

#umidade fora do padrao
print()
print(dataset.loc[(dataset['Umidade']<0)|(dataset['Umidade']>100)])
umidade_mediana = int(sts.median(dataset['Umidade']))
dataset.loc[(dataset['Umidade']<0)|(dataset['Umidade']>100), 'Umidade'] = umidade_mediana

#verificar dados apos tratamento
print(dataset.loc[(dataset['Umidade']<0)|(dataset['Umidade']>100)])

#verificar jogar
jogar_atual = dataset.groupby(['Jogar']).size()
print()
print(jogar_atual)

#atribuimos valor correto
valores_validos = ['sim', 'nao']

moda_jogar = (
    dataset.loc[
        dataset['Jogar'].isin(valores_validos),
        'Jogar'
    ]
    .mode()[0]
)
dataset.loc[~dataset['Jogar'].isin(valores_validos), 'Jogar'] = moda_jogar
#verificar dados apos tratamento
print(dataset.groupby(['Jogar']).size() )

dataset.to_csv('tempo_limpo.csv', sep=';', index=False)
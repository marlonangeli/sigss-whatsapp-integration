import pandas as pd


def get_dataframe(name, age, job):
    df = pd.DataFrame([{
        'name': name,
        'age': age,
        'job': job
    }])
    print(df)
    return df

dados = {
    'name': ['jose', 'maria', 'joao'],
    'age': [20, 30, 40],
    'job': ['engenheiro', 'padeiro', 'vadio']
}


dataframe = pd.DataFrame()

for i in range(len(dados.values())):
    dataframe = dataframe.append(get_dataframe(dados['name'][i], dados['age'][i], dados['job'][i]))

dataframe.reset_index(drop=True, inplace=True)
print(dataframe)
dataframe.drop(0, axis=0, inplace=True)
print(dataframe)
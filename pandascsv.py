import pandas as pd

notas_df = pd.read_csv(r'C:\Users\Jailson\Desktop\PythonSoftex\pandas\notas_alunos.csv', sep = ';')

notas_df['Media'] = (notas_df['Nota_1'] + notas_df['Nota_2']) / 2
notas_df.loc[notas_df['Media'] >= 7, 'Situacao'] = 'Aprovado' 
notas_df.loc[notas_df['Media'] < 7, 'Situacao']  = 'Reprovado'
notas_df.loc[notas_df['Faltas'] > 5, 'Situacao']  = 'Reprovado'  

print(notas_df.head(10))

notas_df.to_csv('alunos_situacao.csv')



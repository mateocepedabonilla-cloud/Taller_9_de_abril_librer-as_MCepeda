import pandas as pd
pd.options.display.float_format = '{:.2f}'.format
datos = {
'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
'turno': ['mañana','tarde','noche','mañana','tarde','noche','mañana','tarde'],
'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
df = pd.DataFrame(datos)
print(df)
print('--- Filas y columnas ---')
print(df.shape)
print('--- Tipo de dato de cada columna ---')
print(df.dtypes)
print('--- Estadisticas basicas ---')
print(df.describe())
print(df['temperatura'])
print(df[['reactor', 'eficiencia']])
print(df.head(3))
print(df[['turno']])
print(df[['reactor', 'incidentes']])
calientes = df[ df['temperatura'] > 88 ]
print('Mediciones con temperatura mayor a 88:')
print(calientes)
mañana = df[ df['turno'] == "mañana" ]
print('Turno mañana:')
print(mañana)
sin_incidentes = df[ df['incidentes'] == 0 ]
print('Sin incidentes:')
print(sin_incidentes)
promedio_temp = df.groupby('reactor')['temperatura'].mean()
print('Temperatura promedio por reactor:')
print(promedio_temp)
ef_turno = df.groupby('turno')['eficiencia'].mean()
print('Eficiencia promedio por turno:')
print(ef_turno)
inc_reactor = df.groupby('reactor')['incidentes'].sum()
print('Total de incidentes por reactor:')
print(inc_reactor)
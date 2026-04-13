import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.2f}'.format
datos = {
    'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
    'turno': ['mañana','tarde','noche','mañana','tarde','noche','mañana','tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
df = pd.DataFrame(datos) 

promedio_temp = df.groupby('reactor')['temperatura'].mean()
plt.figure(figsize=(7, 4))
plt.bar(promedio_temp.index, promedio_temp.values, color='yellow')
plt.title('Temperatura promedio por reactor', fontname='Times New Roman', fontsize=16)
plt.xlabel('Reactor', fontname='Times New Roman', fontsize=12)
plt.ylabel('Temperatura (C)', fontname='Times New Roman', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
plt.scatter(df['temperatura'], df['eficiencia'], color='purple', s=80) 
plt.title('Temperatura vs. Eficiencia', fontname='Times New Roman', fontsize=16)
plt.xlabel('Temperatura (C)', fontname='Times New Roman', fontsize=12)
plt.ylabel('Eficiencia (%)', fontname='Times New Roman', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(df.index, df['eficiencia'], marker='o', linewidth=2, color='green') 
plt.title('Eficiencia por medición', fontname='Times New Roman', fontsize=16)
plt.xlabel('Número de medición', fontname='Times New Roman', fontsize=12)
plt.ylabel('Eficiencia (%)', fontname='Times New Roman', fontsize=12)
plt.tight_layout()
plt.show()
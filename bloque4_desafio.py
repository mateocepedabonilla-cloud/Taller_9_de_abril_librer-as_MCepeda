import pandas as pd
import matplotlib.pyplot as plt
datos = {
    'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
    'turno': ['mañana','tarde','noche','mañana','tarde','noche','mañana','tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
df = pd.DataFrame(datos)
df['estado'] = df['temperatura'].apply(lambda t: 'critico' if t > 90 else 'normal')
print("--- Conteo de estados ---")
print(df['estado'].value_counts())
ef_promedio = df.groupby('reactor')['eficiencia'].mean()
plt.figure(figsize=(7, 4))
colores = ['#fdfd96', '#aec6cf', '#b39eb5']
plt.bar(ef_promedio.index, ef_promedio.values, color=colores, edgecolor='black')
plt.title('Eficiencia promedio por reactor', fontname='Times New Roman',fontsize=16, fontweight='bold')
plt.xlabel('Reactor', fontname='Times New Roman', fontsize=12)
plt.ylabel('Eficiencia (%)', fontname='Times New Roman', fontsize=12)
plt.tight_layout()
plt.show()
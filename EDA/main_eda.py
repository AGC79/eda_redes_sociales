import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings # importa todos los warnings de versión y os ignora
warnings.filterwarnings("ignore")


os.mkdir("eda_gráficos")

social_media = pd.read_csv("Students_Social_Media_Addiction.csv", sep=",")
social_media.head()

# INTRODUCCIÓN: USO DE REDES SOCIALES POR GÉNERO

plt.figure()

plt.style.use('classic')

valores = social_media.groupby("Gender")["Avg_Daily_Usage_Hours"].mean()

valores.index = valores.index.map({
    "Male": "Hombres",
    "Female": "Mujeres"
})
plt.pie(valores, labels=valores.index, autopct='%1.1f%%', colors = ["#1F77B4", "#FF7F0E"])
plt.title("Uso de redes sociales por género")

plt.savefig(".\\eda_gráficos\\grafico_intro.png", dpi=300, bbox_inches='tight') 

# plt.show();

# HIPÓTESIS 1 - GRAFICO 1

df_media_horas = round(social_media.groupby("Affects_Academic_Performance")["Avg_Daily_Usage_Hours"].mean().reset_index(), 1)

plt.figure(figsize=(6,6))
plt.bar(df_media_horas['Affects_Academic_Performance'], df_media_horas['Avg_Daily_Usage_Hours'], color=['skyblue', 'salmon'] )
plt.title("Promedio de horas diarias según percepción de afectación académica", pad=30, fontsize=16)
plt.xlabel("Autopercepción de afectación", labelpad=20, fontsize=14)
plt.ylabel("Horas promedio", labelpad=20, fontsize=14)
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

plt.xticks([0, 1], ["No", "Sí"])

promedios = df_media_horas['Avg_Daily_Usage_Hours']

for indice, valor in enumerate(promedios):
    plt.text(indice, valor + 0.1, f"{valor}", ha='center', fontweight='bold')

plt.xlim(-0.5, len(df_media_horas['Affects_Academic_Performance']) - 0.5)
plt.tight_layout()

plt.savefig(".\\eda_gráficos\\grafico_H1_01.png", dpi=300, bbox_inches='tight') 
# plt.show()
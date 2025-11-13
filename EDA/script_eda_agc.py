import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import os
import warnings # importa todos los warnings de versión y os ignora

warnings.filterwarnings("ignore")


# Crea una carpeta para almacenenar los gráficos descargados
os.makedirs("eda_graficos_agc", exist_ok=True)

# Lee el dataset y crea un dataframe
social_media = pd.read_csv("Students_Social_Media_Addiction.csv", sep=",")


###################################### INTRODUCCIÓN: ###############################
#                                                                                  #
#  GRÁFICO DE TARTA QUE MUESTRA EL PORCENTAJE DE USO DE REDES SOCIALES POR GÉNERO  #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

valores = social_media.groupby("Gender")["Avg_Daily_Usage_Hours"].mean()

# CÓDIGO DEL GRÁFICO

plt.figure()

plt.style.use('classic')

valores.index = valores.index.map({
    "Male": "Hombres",
    "Female": "Mujeres"
})

plt.pie(valores, labels=valores.index, autopct='%1.1f%%', colors = ["#1F77B4", "#FF7F0E"])

plt.title("Uso de redes sociales por género")

plt.savefig(".\\eda_graficos_agc\\grafico_intro.png", dpi=300, bbox_inches='tight') 

# plt.show();


############################ HIPÓTESIS 1 - GRÁFICO 1 ###############################
#                                                                                  #
#     GRÁFICO DE BARRAS CON EL PROMEDIO DE HORAS DE USO DE REDES SOCIALES SEGUN    #
#     PERCEPCION DE AFECTACIÓN EN RENDIMIENTO ACADÉMICO                            #
#                                                                                  #
#################################################################################### 

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

plt.savefig(".\\eda_graficos_agc\\grafico_H1_01.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 1 - GRÁFICO 2 ###############################
#                                                                                  #
#     GRÁFICO DE DISPERSIÓN CON EL PROMEDIO DE HORAS DE USO DE REDES SOCIALES      # 
#     SEGUN PERCEPCION DE AFECTACIÓN EN RENDIMIENTO ACADÉMICO Y GÉNERO             #                               #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

hombres_yes = social_media[(social_media["Affects_Academic_Performance"] == "Yes") & (social_media["Gender"] == "Male")]['Avg_Daily_Usage_Hours']
hombres_no = social_media[(social_media["Affects_Academic_Performance"] == "No") & (social_media["Gender"] == "Male")]['Avg_Daily_Usage_Hours']
mujeres_yes = social_media[(social_media["Affects_Academic_Performance"] == "Yes") & (social_media["Gender"] == "Female")]['Avg_Daily_Usage_Hours']
mujeres_no = social_media[(social_media["Affects_Academic_Performance"] == "No") & (social_media["Gender"] == "Female")]['Avg_Daily_Usage_Hours']

lista_hombres_yes = list(hombres_yes)
lista_hombres_no = list(hombres_no)
lista_mujeres_yes = list(mujeres_yes)
lista_mujeres_no = list(mujeres_no)


x_hombres_no = [-0.1] * len(lista_hombres_no)
x_mujeres_no = [0.1] * len(lista_mujeres_no)
x_hombres_yes = [0.9] * len(lista_hombres_yes)
x_mujeres_yes = [1.1] * len(lista_mujeres_yes)

colores_hombres_no = ["palegreen"] *len(lista_hombres_no)
colores_mujeres_no = ["lightsalmon"] *len(lista_mujeres_no)
colores_hombres_yes = ["palegreen"] *len(hombres_yes)
colores_mujeres_yes = ["lightsalmon"] *len(lista_mujeres_yes)

x_hombres_no_jitter = []

for i in x_hombres_no:
    i = i + np.random.uniform(-0.05, 0.05)
    x_hombres_no_jitter.append(i)

x_mujeres_no_jitter = []

for i in x_mujeres_no:
    i = i + np.random.uniform(-0.05, 0.05)
    x_mujeres_no_jitter.append(i)

x_hombres_yes_jitter = []

for i in x_hombres_yes:
    i = i + np.random.uniform(-0.05, 0.05)
    x_hombres_yes_jitter.append(i)

x_mujeres_yes_jitter = []

for i in x_mujeres_yes:
    i = i + np.random.uniform(-0.05, 0.05)
    x_mujeres_yes_jitter.append(i)

y_total =  lista_hombres_no + lista_mujeres_no + lista_hombres_yes + lista_mujeres_yes
x_total = x_hombres_no_jitter + x_mujeres_no_jitter + x_hombres_yes_jitter + x_mujeres_yes_jitter
colores_total = colores_hombres_no + colores_mujeres_no + colores_hombres_yes + colores_mujeres_yes

media_yes = round(social_media[social_media["Affects_Academic_Performance"] == "Yes"].groupby("Affects_Academic_Performance")["Avg_Daily_Usage_Hours"].mean().reset_index(), 1)
media_no = round(social_media[social_media["Affects_Academic_Performance"] == "No"].groupby("Affects_Academic_Performance")["Avg_Daily_Usage_Hours"].mean().reset_index(), 1)
y_media_yes = media_yes["Avg_Daily_Usage_Hours"].iloc[0]
y_media_no = media_no["Avg_Daily_Usage_Hours"].iloc[0]


## GRÁFICO
plt.figure(figsize=(10,7))

plt.axhline(y=y_media_yes, color='red', linestyle='--', linewidth=2, label='Media de horas SI: 5.5')
plt.axhline(y=y_media_no, color='blue', linestyle='--', linewidth=2, label='Media de horas NO: 3.8')

plt.scatter(x_total, y_total, c=colores_total, alpha=0.8, s=100)

plt.title("Promedio de horas diarias según percepción de afectación académica positiva/negativa", pad=30, fontsize=18)
plt.xlabel("Autopercepción de afectación académica por género", labelpad=20, fontsize=14)
plt.ylabel("Horas diarias de uso de RR.SS", labelpad=20, fontsize=14)
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

p_hombres = plt.scatter([], [], c="palegreen", s=200, label="Hombres")
p_mujeres = plt.scatter([], [], c="lightsalmon", s=200, label="Mujeres")

plt.xticks([0, 1], ["No", "Sí"])
plt.xlim(-0.3, 1.3)
plt.ylim(0, 10)

plt.legend(frameon=False, loc="lower center", fontsize=11, labelspacing=1)

plt.savefig(".\\eda_graficos_agc\\grafico_H1_02.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 1 - GRÁFICO 3 ###############################
#                                                                                  #
#     GRÁFICO DE BARRAS CON EL PROMEDIO DE HORAS DE USO DE REDES SOCIALES SEGUN    #
#     PERCEPCION DE AFECTACIÓN EN RENDIMIENTO ACADÉMICO Y NIVEL ACADÉMICO          #                               #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

medias_niv_acad = social_media.groupby(["Affects_Academic_Performance", "Academic_Level"])["Avg_Daily_Usage_Hours"].mean().reset_index()
medias_niv_acad

dict_mapeo = {"No": 0, "Yes": 1}
medias_niv_acad["Conv"] = medias_niv_acad["Affects_Academic_Performance"].map(dict_mapeo)
medias_niv_acad

niveles = medias_niv_acad['Academic_Level'].unique()

## GRÁFICO

plt.figure(figsize=(8,6))

color = ['gold', 'mediumslateblue', 'indianred']
ancho = 0.2
for i, nivel in enumerate(niveles):
    df_nivel = medias_niv_acad[medias_niv_acad['Academic_Level'] == nivel]
    desplazamiento = (i - 1) * ancho   
    x = df_nivel['Conv'] + desplazamiento
    if nivel == "Graduate":
        nivel = "Graduado universitario"
    elif nivel == "Undergraduate":
        nivel = "Estudiante universitario"
    else:
        nivel = "Educación secundaria"
    plt.bar(x, df_nivel['Avg_Daily_Usage_Hours'], width=ancho, color=color[i], label = nivel)

plt.xticks([0, 1], ["No", "Sí"])
plt.title("Promedio de horas diarias según percepción de afectación académica y nivel académico", pad=30, fontsize=18)
plt.xlabel("Autopercepción de afectación", labelpad=20, fontsize=14)
plt.ylabel("Horas promedio diarias", labelpad=20, fontsize=14)
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

plt.xlim(-0.5, len(df_media_horas['Affects_Academic_Performance']) - 0.5)
plt.legend(frameon=True, loc="lower center", fontsize=11, labelspacing=0.5)
plt.tight_layout()

plt.savefig(".\\eda_graficos_agc\\grafico_H1_03.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 2 - GRÁFICO 1 ###############################
#                                                                                  #
#     GRÁFICO DE BARRAS CON LAS PLATAFORMAS DE REDES SOCIALES MÁS USADAS           #
#     ORDENADAS DE FORMA DESCENDENTE                                               #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

palette_plataformas = {'Instagram': '#E1306C',
                       'Twitter': '#1DA1F2',
                       'TikTok': '#000000',
                       'YouTube': '#FF0000',
                       'Facebook': '#1877F2',
                       'LinkedIn': '#0077B5',
                       'Snapchat': '#FFFC00',
                       'LINE': '#00C300',
                       'KakaoTalk': '#F7C325',
                       'VKontakte': '#4C75A3',
                       'WhatsApp': '#25D366',
                       'WeChat': '#09B83E'}

redes_sociales = social_media["Most_Used_Platform"].value_counts()
colores = [palette_plataformas[plataforma] for plataforma in redes_sociales.index]


# GRÁFICO

plt.figure(figsize=(12,6))

plt.bar(redes_sociales.index, redes_sociales.values, color=colores)

plt.title("Plataformas de redes sociales más utilizadas", pad=20, fontsize=18)
plt.xlabel("Red Social", labelpad=20, fontsize=14)
plt.ylabel("Nº de estudiantes", labelpad=20, fontsize=14)

plt.xticks(rotation=45)

plt.ylim(0, 260)
plt.margins(x=0.03)
plt.tight_layout()

plt.savefig(".\\eda_graficos_agc\\grafico_H2_01.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 2 - GRÁFICO 2 ###############################
#                                                                                  #
#      GRÁFICO DE BARRAS CON LA MEDIA DE ADiCCIÓN SEGÚN LA RED SOCIAL USADA        #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

redes_sociales = social_media["Most_Used_Platform"].value_counts()
orden = redes_sociales.index

y_promedio = social_media["Addicted_Score"].mean()

# GRÁFICO

plt.figure(figsize=(12,6))

sns.barplot(data=social_media, x="Most_Used_Platform", y="Addicted_Score", order=orden, palette=palette_plataformas, ci=None)

plt.axhline(y=y_promedio, color="red", linestyle="--", linewidth=2, label=f"Promedio general: {y_promedio:.2f}")

plt.title("Promedio de adicción por plataforma", pad=20, fontsize=18)
plt.xlabel("Red Social", labelpad=20, fontsize=14)
plt.ylabel("Puntaje promedio de adicción", labelpad=20, fontsize=14)

plt.xticks(rotation=45)
plt.ylim(0, 9)
plt.margins(x=0.03)

plt.tight_layout()

plt.legend(frameon=True, loc="upper center", fontsize=11, labelspacing=0.5)

plt.savefig(".\\eda_graficos_agc\\grafico_H2_02.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 3 - GRÁFICO 1 ###############################
#                                                                                  #
#        GRÁFICO DE CORRELACIÓN ENTRE LAS VARIABLES NUMÉRICAS DEL DATAFRAME        #
#                                                                                  #
#################################################################################### 

plt.figure(figsize=(13,7))

sns.heatmap(social_media.corr(numeric_only=True), 
            annot=True, 
            cmap="seismic", 
            vmin=-1)

plt.title("Correlacciones entre variables numéricas", pad=30, fontsize=20)

plt.tight_layout()

plt.savefig(".\\eda_graficos_agc\\grafico_H3_01.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 3 - GRÁFICO 2 ###############################
#                                                                                  #
#      GRÁFICO DE DISPERSIÓN QUE RELACIONA EL NÚMERO DE HORAS DE USO DE REDES      #
#      SOCIALES CON EL NIVEL DE SALUD MENTAL Y LAS HORAS DE SUEÑO                  #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

df_salud_adiccion_sueno = social_media[["Addicted_Score", "Mental_Health_Score", "Sleep_Hours_Per_Night"]]
df_salud_adiccion_sueno

# GRÁFICO

plt.figure(figsize=(10,6))

df_salud_adiccion_sueno['Addicted_Jitter'] = df_salud_adiccion_sueno['Addicted_Score'] + np.random.normal(0, 0.2, len(df_salud_adiccion_sueno))
df_salud_adiccion_sueno['Mental_Jitter'] = df_salud_adiccion_sueno['Mental_Health_Score'] + np.random.normal(0, 0.2, len(df_salud_adiccion_sueno))

sns.scatterplot(x='Addicted_Jitter',
                y='Mental_Jitter',
                hue='Sleep_Hours_Per_Night',     
                size='Sleep_Hours_Per_Night',    
                sizes=(1, 300),
                palette='inferno',
                alpha=0.7,
                data=df_salud_adiccion_sueno)

plt.title('Relación entre adicción, salud mental y horas de sueño', pad=20, fontsize=18)
plt.xlabel('Adicción a redes sociales', labelpad=20, fontsize=14)
plt.ylabel('Salud mental', labelpad=20, fontsize=14)

plt.xlim(0, 10)
plt.xlim(0, 10)

plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 11, 1))

plt.legend(frameon=True, loc="lower center", fontsize=13, labelspacing=1, title="Horas de sueño")

plt.savefig(".\\eda_graficos_agc\\grafico_H3_02.png", dpi=300, bbox_inches='tight') 
# plt.show();


############################ HIPÓTESIS 4 - GRÁFICO 1 ###############################
#                                                                                  #
#      GRÁFICO DE BARRAS QUE RELACIONA EL NÚMERO DE HORAS DE USO DE REDES          #
#      SOCIALES CON EL NIVEL DE ADICCIÓN SEGÚN ESTADO SENTIMENTLA                  #
#                                                                                  #
#################################################################################### 

## PREPARACIÓN DE DATOS

df_relaciones = social_media[["Avg_Daily_Usage_Hours", "Addicted_Score", "Relationship_Status"]]
df_relaciones

df_relaciones_horas = df_relaciones.groupby("Relationship_Status")["Avg_Daily_Usage_Hours"].mean().reset_index()
df_relaciones_horas

df_relaciones_adiccion = df_relaciones.groupby("Relationship_Status")["Addicted_Score"].mean().reset_index()
df_relaciones_adiccion

df_relaciones_horas_adiccion = pd.merge(df_relaciones_horas, df_relaciones_adiccion).reset_index(drop=True)
df_relaciones_horas_adiccion

df_melted = df_relaciones_horas_adiccion.melt(
    id_vars='Relationship_Status',
    value_vars=['Avg_Daily_Usage_Hours', 'Addicted_Score'],
    var_name='Variable',
    value_name='Valor'
)

df_melted['Variable'] = df_melted['Variable'].replace({
    'Avg_Daily_Usage_Hours': 'Horas diarias de uso',
    'Addicted_Score': 'Nivel de adicción'
})

# GRÁFICO

fig = px.bar(df_melted,
             x='Relationship_Status',
             y='Valor',
             color='Variable',
             barmode='group',
             title='Relación entre horas de uso y adicción según estado sentimental',
             text=None,
             color_discrete_sequence=['#1f77b4', '#ff7f0e'],
             labels={'Relationship_Status': 'Estado sentimental',
                     'Valor': 'Promedio',
                     'Variable': 'Indicador'})

fig.update_layout(template='plotly_white',
                  xaxis_title='Estado sentimental',
                  yaxis_title='Escala de promedios',
                  legend_title='Indicador',
                  yaxis=dict(range=[0, 10]))

fig.write_image(".\\eda_graficos_agc\\grafico_H4_01.png")
# fig.show()

print("Se han descargado correctamente todos los gráficos.")

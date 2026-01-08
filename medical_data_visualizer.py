import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Função principal que carrega e pré-processa os dados
def calculate_medical_data(csv_file='medical_examination.csv'):
    # 1. Importa os dados do arquivo CSV especificado
    df = pd.read_csv(csv_file)

    # 2. Adiciona a coluna 'overweight' (sobrepeso) baseada no IMC
    bmi = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = np.where(bmi > 25, 1, 0)

    # 3. Normaliza os dados de colesterol e glicose (0=bom, 1=ruim)
    df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
    df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
    
    # 10. Limpeza de dados (Instrução 10 da imagem 3)
    # Remove os pacientes com dados inconsistentes/outliers
    df = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    return df

def draw_cat_plot():
    df = calculate_medical_data()
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.value_counts().reset_index(name='total')
    
    fig = sns.catplot(
        data=df_cat, 
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        kind='bar'
    ).fig 
    
    plt.tight_layout()
    return fig

def draw_heat_map():
    df = calculate_medical_data()
    corr = df.corr().round(1)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True,      
        fmt='.1f',       
        cmap='coolwarm', 
        center=0,        
        linewidths=.5,   
        cbar_kws={"shrink": .5}
    )
    
    return fig

import matplotlib
matplotlib.use('Agg')  # Configura o backend não interativo

import matplotlib.pyplot as plt
import seaborn as sns  # Biblioteca para paleta de cores
from matplotlib.dates import DateFormatter

# Configurações gerais para estilo
sns.set(style="whitegrid")  # Define o estilo do grid para tornar os gráficos mais elegantes
plt.rcParams.update({'font.size': 12})  # Define o tamanho da fonte padrão

def plot_temperature(df):
    plt.figure(figsize=(12, 6))
    
    # Define uma paleta de cores
    colors = sns.color_palette("husl", len(df['cidade'].unique()))
    
    for i, city in enumerate(df['cidade'].unique()):
        city_data = df[df['cidade'] == city]
        
        # Adiciona linhas de temperatura para cada cidade com marcadores
        plt.plot(city_data['data'], city_data['temperatura'], label=city,
                 color=colors[i], marker='o', linestyle='-', linewidth=2, markersize=6)

    # Detalhes do gráfico
    plt.title('Temperatura ao longo do tempo', fontsize=16, fontweight='bold')
    plt.xlabel('Data', fontsize=14)
    plt.ylabel('Temperatura (°C)', fontsize=14)
    plt.legend(title='Cidade', loc='best', fontsize=10)  # Legenda com título
    
    # Formata a data no eixo x
    plt.xticks(rotation=45)
    date_form = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_form)
    
    # Adiciona uma grid mais leve e define os limites do eixo y com margem
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(df['temperatura'].min() - 2, df['temperatura'].max() + 2)
    
    # Ajusta o layout e salva a figura
    plt.tight_layout()
    plt.savefig('temperatura.png', dpi=300)  # DPI mais alto para melhor resolução
    plt.close()

def plot_humidity(df):
    plt.figure(figsize=(12, 6))
    
    # Define uma paleta de cores
    colors = sns.color_palette("cool", len(df['cidade'].unique()))
    
    for i, city in enumerate(df['cidade'].unique()):
        city_data = df[df['cidade'] == city]
        
        # Adiciona linhas de umidade para cada cidade com marcadores
        plt.plot(city_data['data'], city_data['umidade'], label=city,
                 color=colors[i], marker='s', linestyle='--', linewidth=2, markersize=6)

    # Detalhes do gráfico
    plt.title('Umidade ao longo do tempo', fontsize=16, fontweight='bold')
    plt.xlabel('Data', fontsize=14)
    plt.ylabel('Umidade (%)', fontsize=14)
    plt.legend(title='Cidade', loc='best', fontsize=10)  # Legenda com título
    
    # Formata a data no eixo x
    plt.xticks(rotation=45)
    date_form = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_form)
    
    # Adiciona uma grid mais leve e define os limites do eixo y com margem
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(df['umidade'].min() - 5, df['umidade'].max() + 5)
    
    # Ajusta o layout e salva a figura
    plt.tight_layout()
    plt.savefig('umidade.png', dpi=300)  # DPI mais alto para melhor resolução
    plt.close()

import sys
import os

# Adiciona o diretório src ao PYTHONPATH
src_dir = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_dir)

# Importa main do módulo src
from main import FILE_PATH, fetch_weather_data, plot_temperature, plot_humidity

# Executa main
if __name__ == "__main__":
    df = fetch_weather_data(FILE_PATH)
    
    if df is not None:
        print("Dados carregados:")
        print(df.head())  # Exibe as primeiras linhas do DataFrame
        plot_temperature(df)
        plot_humidity(df)
    else:
        print("Falha ao carregar os dados.")

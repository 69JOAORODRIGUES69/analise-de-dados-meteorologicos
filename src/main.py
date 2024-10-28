from src.api_data import fetch_weather_data
from src.data_analysis import plot_temperature, plot_humidity

FILE_PATH = "data/weather_data.csv"  # Caminho para o arquivo CSV

if __name__ == "__main__":
    print(f"Carregando dados do arquivo: {FILE_PATH}")
    df = fetch_weather_data(FILE_PATH)
    
    if df is not None:
        print("Dados carregados:")
        print(df.head())  # Exibe as primeiras linhas do DataFrame
    else:
        print("Falha ao carregar os dados.")
    
    if df is not None and not df.empty:
        plot_temperature(df)
        plot_humidity(df)
    else:
        print("Nenhum dado encontrado ou o DataFrame está vazio.")

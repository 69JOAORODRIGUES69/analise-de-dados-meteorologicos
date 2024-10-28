import pandas as pd

def fetch_weather_data(file_path):
    df = pd.read_csv(file_path)
    return df
import requests
import pandas as pd
import zipfile
import io
import os

# Lista dos links dos arquivos ZIP (2023, 2024, 2025)
zip_links = [
    {
        "ano": 2023,
        "url": "https://www.transparencia.df.gov.br/arquivos/Remuneracao_2023.zip"
    },
    {
        "ano": 2024,
        "url": "https://www.transparencia.df.gov.br/arquivos/Remuneracao_2024.zip"
    },
    {
        "ano": 2025,
        "url": "https://www.transparencia.df.gov.br/arquivos/Remuneracao_2025.zip"
    }
]

os.makedirs("data", exist_ok=True)

for link in zip_links:
    print(f"Baixando e processando ano {link['ano']}...")
    r = requests.get(link['url'])
    z = zipfile.ZipFile(io.BytesIO(r.content))
    # Pega o primeiro arquivo CSV dentro do ZIP
    csv_name = [f for f in z.namelist() if f.lower().endswith(".csv")][0]
    with z.open(csv_name) as f:
        # Ajuste o encoding e separador se necessário!
        df = pd.read_csv(f, sep=';', encoding='latin1',dtype=str)
        parquet_path = f"data/servidores_{link['ano']}_raw.parquet"
        df.to_parquet(parquet_path, index=False)
        print(f"Salvo: {parquet_path}")

print("Concluído!")

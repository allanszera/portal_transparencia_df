from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

parquet_files = os.getenv("PARQUETS").split(',')

dfs = [pd.read_parquet(path) for path in parquet_files]
df = pd.concat(dfs, ignore_index=True)

df['LÍQUIDO'] = df['LÍQUIDO'].str.replace(',', '.', regex=False)
df['LÍQUIDO'] = pd.to_numeric(df['LÍQUIDO'], errors='coerce')
df['ANO'] = df['ANO'].astype(int)
df['MÊS'] = df['MÊS'].astype(int)

# Lista das colunas que precisam ser transformadas para float
colunas_valores = [
    "REMUNERAÇÃO BÁSICA",
    "BENEFÍCIOS",
    "VALOR DA FUNÇÃO",
    "COMISSÃO CONSELHEIRO",
    "HORA EXTRA",
    "VERBAS EVENTUAIS",
    "VERBAS JUDICIAIS",
    "DESCONTOS A MAIOR",
    "LICENÇA PRÊMIO",
    "IRRF",
    "SEG. SOCIAL",
    "TETO REDUTOR",
    "OUTROS RECEBIMENTOS",
    "OUTROS DESCONTOS OBRIGATÓRIOS",
    "PAGAMENTOS A MAIOR",
    "BRUTO"
]

for col in colunas_valores:
    df[col] = (
        df[col].astype(str)
        .str.replace('.', '', regex=False)      
        .str.replace(',', '.', regex=False)     
        .str.replace('R$', '', regex=False)     
        .str.strip()                            
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')



print(df.dtypes)
print(df[['MÊS','ANO']].drop_duplicates())
print(df['LÍQUIDO'])




# Salve o DataFrame tratado em um único arquivo Parquet#
df.to_parquet("data/servidores_tratado.parquet", index=False)

print("Arquivo data/servidores_tratado.parquet salvo com sucesso!")

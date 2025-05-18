import streamlit as st
import duckdb
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout="wide")

parquet_path = 'C:/Users/allan/OneDrive/portal_transparencia_df/data/servidores_tratado.parquet'

# Consultas SQL
sql1 = f"""
SELECT ÓRGÃO, sum(LÍQUIDO) as SOMA_SALARIO
FROM read_parquet('{parquet_path}')
GROUP BY ÓRGÃO
ORDER BY SOMA_SALARIO DESC
LIMIT 10
"""
sql2 = f"""
SELECT CARGO, ÓRGÃO, SITUAÇÃO, max(LÍQUIDO) as MAIOR_LIQUIDO
FROM read_parquet('{parquet_path}')
GROUP BY CARGO, ÓRGÃO, SITUAÇÃO
ORDER BY MAIOR_LIQUIDO DESC
LIMIT 10
"""
sql3 = f"""
SELECT CARGO, ÓRGÃO, SITUAÇÃO, max(LÍQUIDO) as MAIOR_LIQUIDO
FROM read_parquet('{parquet_path}')
WHERE SITUAÇÃO = 'ATIVO'
GROUP BY CARGO, ÓRGÃO, SITUAÇÃO
ORDER BY MAIOR_LIQUIDO DESC
LIMIT 10
"""

# Opções do "carrossel"
pages = [
    "Resumo do Projeto",
    "Top 10 Órgãos com Maior Soma de Salários",
    "Top 10 Maiores Salários Líquidos por Cargo",
    "Top 10 Maiores Salários Líquidos entre Servidores Ativos",
    "Storytelling Final"
]

# Barra de navegação estilo carrossel
page = st.selectbox("Navegue entre as páginas do carrossel 👇", pages)

if page == "Resumo do Projeto":
    st.title("Projeto Educacional de ETL com Dados Públicos do DF")
    st.markdown("""
    🚨 **Você sabia?**  
    - O Instituto de Previdência dos Servidores do DF lidera a folha de pagamento do DF.
    - Cargos com maiores salários estão em gestão, fiscalização e segurança pública.
    - A maior parte dos salários mais altos é de aposentados e pensionistas.
    - Entre ativos, as maiores remunerações são da Segurança Pública.

    ⚠️ **Este projeto é apenas para fins educacionais.**
    """)
    st.markdown("""
    **Como funciona o pipeline ETL:**
    1️⃣ Extração dos dados do Portal da Transparência  
    2️⃣ Tratamento e padronização dos dados  
    3️⃣ Análise com SQL e visualização  
    4️⃣ Storytelling  
    """)

if page == "Top 10 Órgãos com Maior Soma de Salários":
    st.header("Top 10 Órgãos com Maior Soma de Salários")
    df_orgaos = duckdb.query(sql1).to_df()
    df_orgaos['SOMA_SALARIO'] = df_orgaos['SOMA_SALARIO'].apply(
        lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    st.dataframe(df_orgaos)
    st.code(sql1, language="sql")

if page == "Top 10 Maiores Salários Líquidos por Cargo":
    st.header("Top 10 Maiores Salários Líquidos por Cargo")
    df_cargos = duckdb.query(sql2).to_df()
    df_cargos['MAIOR_LIQUIDO'] = df_cargos['MAIOR_LIQUIDO'].apply(
        lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    st.dataframe(df_cargos)
    st.code(sql2, language="sql")

if page == "Top 10 Maiores Salários Líquidos entre Servidores Ativos":
    st.header("Top 10 Maiores Salários Líquidos entre Servidores Ativos")
    df_ativos = duckdb.query(sql3).to_df()
    df_ativos['MAIOR_LIQUIDO'] = df_ativos['MAIOR_LIQUIDO'].apply(
        lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    st.dataframe(df_ativos)
    st.code(sql3, language="sql")

if page == "Storytelling Final":
    st.header("Resumo e Interpretação dos Dados")
    st.markdown("""
    - O Instituto de Previdência dos Servidores do DF lidera a soma dos salários, evidenciando o peso dos benefícios previdenciários.
    - Os maiores salários líquidos concentram-se em cargos de gestão, fiscalização, educação e segurança pública.
    - Entre os maiores salários, predominam aposentados e pensionistas, reforçando a relevância da previdência.
    - Entre servidores ativos, destacam-se os cargos das forças de segurança (Polícia Militar, Polícia Civil), com altos salários decorrentes de adicionais, tempo de carreira e riscos da profissão.
    - Os altos salários resultam da soma de carreira longa, benefícios legais, gratificações, acúmulo de funções e, por vezes, decisões judiciais.

    **Para exportar cada página, use Ctrl+P no navegador e salve como PDF ou PNG!**
    """)


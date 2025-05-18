import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(layout="wide")

st.title('Análise da Folha de Pagamento dos Servidores do Distrito Federal')
st.markdown("""
O gasto com pessoal é uma das principais despesas do setor público. Esta análise, baseada nos dados do Portal da Transparência DF, revela quem são os maiores beneficiários, quais órgãos concentram mais recursos e como as carreiras públicas estão estruturadas no Distrito Federal.
""")

parquet_path = 'C:/Users/allan/OneDrive/portal_transparencia_df/data/servidores_tratado.parquet'

# ------------------------- TABELA 1 -----------------------------
st.header('Top 10 Órgãos com Maior Soma de Salários')

sql1 = f"""
SELECT ÓRGÃO, sum(LÍQUIDO) as SOMA_SALARIO
FROM read_parquet('{parquet_path}')
GROUP BY ÓRGÃO
ORDER BY SOMA_SALARIO DESC
LIMIT 10
"""
df_orgaos = duckdb.query(sql1).to_df()
df_orgaos['SOMA_SALARIO'] = df_orgaos['SOMA_SALARIO'].apply(
    lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
st.dataframe(df_orgaos)
st.code(sql1, language="sql")

# ------------------------- TABELA 2 -----------------------------
st.header('Top 10 Maiores Salários Líquidos por Cargo')

sql2 = f"""
SELECT CARGO, ÓRGÃO, SITUAÇÃO, max(LÍQUIDO) as MAIOR_LIQUIDO
FROM read_parquet('{parquet_path}')
GROUP BY CARGO, ÓRGÃO, SITUAÇÃO
ORDER BY MAIOR_LIQUIDO DESC
LIMIT 10
"""
df_cargos = duckdb.query(sql2).to_df()
df_cargos['MAIOR_LIQUIDO'] = df_cargos['MAIOR_LIQUIDO'].apply(
    lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
st.dataframe(df_cargos)
st.code(sql2, language="sql")

# ------------------------- TABELA 3 -----------------------------
st.header('Top 10 Maiores Salários Líquidos entre Servidores Ativos')

sql3 = f"""
SELECT CARGO, ÓRGÃO, SITUAÇÃO, max(LÍQUIDO) as MAIOR_LIQUIDO
FROM read_parquet('{parquet_path}')
WHERE SITUAÇÃO = 'ATIVO'
GROUP BY CARGO, ÓRGÃO, SITUAÇÃO
ORDER BY MAIOR_LIQUIDO DESC
LIMIT 10
"""
df_ativos = duckdb.query(sql3).to_df()
df_ativos['MAIOR_LIQUIDO'] = df_ativos['MAIOR_LIQUIDO'].apply(
    lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
st.dataframe(df_ativos)
st.code(sql3, language="sql")

# ------------------------- STORYTELLING -----------------------------
st.header('Resumo e Interpretação dos Dados')
st.markdown("""
- O Instituto de Previdência dos Servidores do DF lidera a soma dos salários, evidenciando o peso dos benefícios previdenciários.
- Os maiores salários líquidos concentram-se em cargos de gestão, fiscalização, educação e segurança pública.
- Entre os maiores salários, predominam aposentados e pensionistas, reforçando a relevância da previdência.
- Entre servidores ativos, destacam-se os cargos das forças de segurança (Polícia Militar, Polícia Civil), com altos salários decorrentes de adicionais, tempo de carreira e riscos da profissão.
- As funções desses órgãos vão da proteção da vida e ordem pública até a manutenção de serviços essenciais como energia e educação.
- Os altos salários resultam da soma de carreira longa, benefícios legais, gratificações, acúmulo de funções e, por vezes, decisões judiciais.
""")

st.markdown("""
**Para exportar este relatório para PDF, utilize o atalho do navegador (Ctrl+P) e selecione "Salvar como PDF".**
""")

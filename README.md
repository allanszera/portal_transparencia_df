
# Projeto ETL - Portal da Transparência DF

Este projeto de estudo tem como objetivo realizar um pipeline ETL (Extract, Transform, Load) dos dados de remuneração de servidores públicos do Distrito Federal, disponíveis no Portal da Transparência DF.

## 📦 Estrutura do Projeto

```
PORTAL_...
│
├── .venv/                # Ambiente virtual Python (ignorado pelo git)
├── data/                 # Dados brutos e processados (ignorado pelo git)
├── src/                  # Scripts principais do pipeline
│   ├── extract.py        # Extração dos dados do portal
│   ├── transform.py      # Limpeza e transformação dos dados
│   └── load.py           # Salvamento dos dados processados (ex: Parquet)
├── .env                  # Variáveis de ambiente (ignorado pelo git)
├── .gitignore            # Padrões de arquivos/pastas ignorados
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

---

## ⚙️ Como rodar o projeto

1. **Clone o repositório e entre na pasta do projeto**

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv .venv
   # Ative no Linux/Mac:
   source .venv/bin/activate
   # Ative no Windows:
   .venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env`** (se necessário)
   - Coloque suas variáveis de ambiente ou deixe vazio se não precisar.

5. **Execute as etapas do pipeline**
   - **Extração:**
     ```bash
     python src/extract.py
     ```
   - **Transformação:**
     ```bash
     python src/transform.py
     ```
   - **Carga (salvar dados processados):**
     ```bash
     python src/load.py
     ```

---

## 📝 Descrição dos Arquivos

- **src/extract.py**: Coleta os dados do Portal da Transparência DF e salva na pasta `data/`.
- **src/transform.py**: Realiza limpeza, padronização e outras transformações necessárias nos dados brutos.
- **src/load.py**: Salva os dados transformados em formato Parquet, CSV ou outro formato eficiente, na pasta `data/`.

---

## 🛑 O que está ignorado no git?

Veja o arquivo `.gitignore`:

```
# Ambiente virtual Python
.venv/
venv/
ENV/
env/

# Dados brutos e processados
data/
*.csv
*.parquet

# Variáveis de ambiente
.env
*.env

# Cache do Python
__pycache__/
*.py[cod]
*$py.class

# Notebooks e logs
.ipynb_checkpoints/
*.log

# Arquivos temporários do sistema
.DS_Store
Thumbs.db
```

---

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas: ver `requirements.txt` (por exemplo: playwright, pandas, pyarrow, matplotlib, seaborn, jupyter, etc.)

---

## 📌 Observações

- O diretório `data/` é ignorado no git, então os dados baixados e processados não serão versionados.
- Certifique-se de que o Portal da Transparência DF esteja online para a etapa de extração funcionar corretamente.
- Este projeto é apenas para fins de estudo.

---

Qualquer dúvida ou sugestão, é só chamar! 🚀

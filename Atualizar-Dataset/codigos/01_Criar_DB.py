import pandas as pd
from pathlib import Path
import os

script_dir = Path(__file__).parent.parent
projeto_raiz = script_dir.parent

caminho_db_a = projeto_raiz / 'Ajuste-Colunas-Numericas' / "DB.xlsx"
caminho_db_b = projeto_raiz / 'Ajuste-Colunas-Booleanas' / "colunas_combinadas.xlsx"

caminho_pasta_saida = script_dir / "datasets"
caminho_arquivo_saida_csv = script_dir / "datasets" /"DB_novo.csv"

os.makedirs(caminho_pasta_saida, exist_ok=True)

try:
    print("=== Juntando Colunas Numericas e Booleanas num só DB.... ===")
    db_a = pd.read_excel(caminho_db_a)
    db_b = pd.read_excel(caminho_db_b)
    dataframes = [db_a, db_b]
    df_combined = pd.concat(dataframes, axis=1)

    # Salvando em csv
    df_combined.to_csv(caminho_arquivo_saida_csv, index=False)

    print("✅Novo Banco de Dados Gerado com Sucesso!!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
import pandas as pd
import glob
import os

print("\n=== Iniciando processo de juntar colunas num só dataset... ===")

script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

saida_arquivo_xlsx = os.path.join(projeto_raiz, "colunas_combinadas.xlsx")

pasta_arquivos = os.path.join(projeto_raiz, "csv-gerados", "*.csv")
caminho_arquivos = sorted(glob.glob(pasta_arquivos))

dataframes = []

for arquivo in caminho_arquivos:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

df_combined = pd.concat(dataframes, axis=1)
df_combined.to_excel(saida_arquivo_xlsx, index=False)

print("✅Arquivos combinados com sucesso!!")
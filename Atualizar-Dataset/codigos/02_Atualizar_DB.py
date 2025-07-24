import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent.parent
projeto_raiz = script_dir.parent

caminho_db_a = script_dir / "datasets" / "relatorios.csv"
caminho_db_b = script_dir / "datasets" / "DB_novo.csv"

arquivo_saida_xlsx = projeto_raiz / "Dataset.xlsx"
arquivo_saida_csv = projeto_raiz / "relatorios.csv"

df_a = pd.read_csv(caminho_db_a)
df_b = pd.read_csv(caminho_db_b)

df_a.drop(columns=['Ação',"Filtro"], inplace=True) 

# Agora o df_a já não tem mais a coluna "Ação"
print("\n=== Concatenando Banco de Dados antigo com o novo... ===")

df_final = pd.concat([df_a, df_b], ignore_index=True)

df_final.to_csv(arquivo_saida_xlsx, index=False)
df_final.to_csv(arquivo_saida_csv, index=False)

print("✅Banco de dados Atualizado com Sucesso!!")

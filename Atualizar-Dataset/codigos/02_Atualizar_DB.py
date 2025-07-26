import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent.parent
projeto_raiz = script_dir.parent

caminho_db_a = script_dir / "datasets" / "relatorios.csv"
caminho_db_b = script_dir / "datasets" / "DB_novo.csv"

arquivo_saida_xlsx = projeto_raiz / "Dataset.xlsx"
arquivo_saida_csv = projeto_raiz / "relatorios.csv"

try: 
    df_a = pd.read_csv(caminho_db_a)
    df_b = pd.read_csv(caminho_db_b)

    # Remove colunas específicas do dataset antigo
    # O 'inplace=True' modifica o DataFrame diretamente sem retornar uma cópia
    df_a.drop(columns=['Ação',"Filtro"], inplace=True) 

    # Agora o df_a já não tem mais a coluna "Ação"
    print("\n=== Concatenando Banco de Dados antigo com o novo... ===")

    # Concatena os DataFrames verticalmente (empilhando as linhas)
    # ignore_index=True redefine o índice do DataFrame final
    df_final = pd.concat([df_a, df_b], ignore_index=True)

    df_final.to_csv(arquivo_saida_xlsx, index=False)
    df_final.to_csv(arquivo_saida_csv, index=False)

    print("✅Banco de dados Atualizado com Sucesso!!")
    
except FileNotFoundError as e:
    print(f"Erro: Um dos arquivos de entrada não foi encontrado. Verifique se eles existem nos caminhos esperados: {e}")
except KeyError as e:
    print(f"Erro: Uma das colunas a serem removidas não foi encontrada no dataset antigo: {e}")    
except Exception as e:
    print(f"Ocorreu um erro inesperado durante a atualização do banco de dados: {e}")

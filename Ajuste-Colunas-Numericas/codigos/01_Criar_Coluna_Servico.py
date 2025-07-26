import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

caminho_db_a = os.path.join(projeto_raiz, 'arquivos-xlsx', "BD-Extensão.xlsx")
caminho_arquivo_saida = os.path.join(projeto_raiz, 'arquivos-xlsx', "BD-Combinado.xlsx")

MAPA_NOME_PARA_SIGLA = {1: "Avaliação", 2: "Consultoria", 3: "Apuração"}
mapa_para_numerico = {sigla: numero for numero, sigla in MAPA_NOME_PARA_SIGLA.items()}

try:
    print("\n=== Iniciando processo de gerar dataset com valores númericos... ===")
    df_a = pd.read_excel(caminho_db_a)
    if "Serviço" in df_a.columns:
        df_a["Serviço"] = df_a["Serviço"].map(mapa_para_numerico)
        df_a["Serviço"] = df_a["Serviço"].fillna(99)
        df_a.to_excel(caminho_arquivo_saida, index=False)
        print("✅Coluna Serviço Atualizada com Sucesso!!")
    else:
        print(f"ℹ️ Coluna 'Serviço' não encontrada no arquivo '{os.path.basename(caminho_db_a)}'. Nenhuma alteração de serviço feita.")        
except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")

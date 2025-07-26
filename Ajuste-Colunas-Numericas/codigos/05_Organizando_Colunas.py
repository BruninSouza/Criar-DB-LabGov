import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

caminho_arquivo = os.path.join(projeto_raiz, "DB.xlsx")

try:
    # Renomeando Colunas para nomes adequados
    df = pd.read_excel(caminho_arquivo)
    df_renomeado = df.rename(columns={"Título": "Nome", "Publicação": "Data"})

    colunas_organizadas = ["ID", "Nome", "Serviço", "Grupo", "Avaliação", "Data", "Ano", "Governo", "UF"]
    
    colunas_faltando = [col for col in colunas_organizadas if col not in df_renomeado.columns]    
    if colunas_faltando:
        print(f"Atenção: As seguintes colunas esperadas não foram encontradas no DataFrame: {colunas_faltando}. Elas podem aparecer como NaN no resultado final.")

    df_copy = df_renomeado
    df_copy = df_copy[colunas_organizadas]

    df_copy.to_excel(caminho_arquivo, index=False)

    print("✅Colunas Renomeadas e Organizadas com Sucesso!!")

except FileNotFoundError as e:
    print(f"Erro: Arquivo '{os.path.basename(caminho_arquivo)}' não encontrado. Verifique se o caminho e o nome do arquivo estão corretos. Detalhes: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado durante a renomeação e organização das colunas: {e}")

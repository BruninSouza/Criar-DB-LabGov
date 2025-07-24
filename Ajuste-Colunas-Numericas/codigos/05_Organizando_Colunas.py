import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

caminho_arquivo = os.path.join(projeto_raiz, "DB.xlsx")

# Renomeando Colunas para nomes adequados
df = pd.read_excel(caminho_arquivo)
df_renomeado = df.rename(columns={"Título": "Nome", "Publicação": "Data"})

colunas_organizadas = ["ID", "Nome", "Serviço", "Grupo", "Avaliação", "Data", "Ano", "Governo", "UF"]

df_copy = df_renomeado
df_copy = df_copy[colunas_organizadas]

df_copy.to_excel(caminho_arquivo, index=False)

print("✅Colunas Renomeadas e Organizadas com Sucesso!!")

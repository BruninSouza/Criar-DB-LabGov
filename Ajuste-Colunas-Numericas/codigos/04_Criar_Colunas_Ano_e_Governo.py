import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

caminho_arquivo = os.path.join(projeto_raiz, "DB.xlsx")

# Criando Coluna Ano
df = pd.read_excel(caminho_arquivo)
df['Publicação'] = pd.to_datetime(df['Publicação'])
df['Ano'] = df['Publicação'].dt.year

print("✅Coluna Ano Criada com Sucesso!!")


# Criando Coluna Governo
df['Governo'] = 3 # O código atribuído a ela é o referente ao governo atual

# Salva as novas colunas no dataset principal
df_copy = df
df_copy.to_excel(caminho_arquivo, index=False)

print("✅Coluna Governo Criada com Sucesso!!")

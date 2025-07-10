import pandas as pd
import re

def extrair_sigla(texto_da_celula):
    """
    Verifica se alguma sigla de estado está presente no texto.
    Retorna a primeira sigla que encontrar, ou o texto original se nenhuma for encontrada.
    """
    # Converte o conteúdo da célula para string para evitar erros com números ou outros tipos
    texto_str = str(texto_da_celula)

    for sigla in siglas_estados:
        # Cria um padrão de busca (RegEx) para encontrar a sigla como uma palavra isolada
        # \b significa "fronteira de palavra". Isso evita que 'SP' seja encontrado em 'transporte'
        padrao = r'\b' + sigla + r'\b'
        if re.search(padrao, texto_str, re.IGNORECASE): # re.IGNORECASE torna a busca não sensível a maiúsculas/minúsculas
            return sigla # Retorna a sigla encontrada
            
    return texto_da_celula

siglas_estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
    "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN",
    "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

df = pd.read_excel("DB_com_grupo.xlsx")

try:
    print("--- DataFrame Original ---")
    print(df)

    # Aplica a função 'extrair_sigla' a cada célula da coluna "Localidade(s)"
    df['Localidade(s)'] = df['Localidade(s)'].apply(extrair_sigla)

    print("\n--- DataFrame com Localidades Padronizadas ---")
    print(df)

    # Salvar o resultado
    df.to_excel("DB_Definitivo.xlsx", index=False)
    print("\nArquivo 'DB_Definitivo.xlsx' salvo com sucesso!")

except FileNotFoundError:
    print("Erro: Arquivo 'dados_localidades_texto.xlsx' não encontrado.")
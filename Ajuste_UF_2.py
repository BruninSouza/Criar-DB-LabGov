import pandas as pd
import re

# Resumindo localidades em siglas

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

df = pd.read_excel("arquivos-xslx/DB.xlsx")

try:
    print("--- DataFrame Original ---")
    print(df)

    # Aplica a função 'extrair_sigla' a cada célula da coluna "Localidade(s)"
    df['Localidade(s)'] = df['Localidade(s)'].apply(extrair_sigla)

    print("\n--- DataFrame com Localidades Padronizadas ---")
    print(df)

    # Salvar o resultado
    df.to_excel("arquivos-xslx/DB.xlsx", index=False)
    print("\nArquivo salvo com sucesso!")

except FileNotFoundError:
    print("Erro: Arquivo 'dados_localidades_texto.xlsx' não encontrado.")

# COnvertendo para numerico

mapa_localidades_correto = {
    1: "AC", 2: "AL", 3: "AM", 4: "AP", 5: "BA", 6: "CE", 7: "DF",
    8: "ES", 9: "GO", 10: "MA", 11: "MG", 12: "MS", 13: "MT", 14: "PA",
    15: "PB", 16: "PE", 17: "PI", 18: "PR", 19: "RJ", 20: "RN", 21: "RO",
    22: "RR", 23: "RS", 24: "SC", 25: "SE", 26: "SP", 27: "TO"
}

mapa_para_numerico = {sigla: numero for numero, sigla in mapa_localidades_correto.items()}

# 2. Carregar o arquivo com as siglas dos estados
try:
    df = pd.read_excel("arquivos-xslx/DB.xlsx")
    print("--- DataFrame Original (com siglas) ---")
    print(df)

    # 3. Aplicar o mapa invertido para converter siglas em números
    # O .map() irá substituir cada sigla pelo número correspondente
    # Valores que não estão no mapa (como 'Sem localidade definida') se tornarão NaN
    df['Localidade(s)'] = df['Localidade(s)'].map(mapa_para_numerico)

    print("\n--- DataFrame Convertido (com códigos numéricos) ---")
    print(df)

    # 4. Salvar o resultado final
    df.to_excel("arquivos-xslx/DB.xlsx", index=False)
    print("\nArquivo 'DB.xlsx' salvo com sucesso!")

except FileNotFoundError:
    print("Erro: Arquivo 'dados_localidades_padronizadas.xlsx' não encontrado.")
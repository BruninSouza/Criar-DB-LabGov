import pandas as pd
import numpy as np

mapa_localidades_correto = {
    1: "AC", 2: "AL", 3: "AM", 4: "AP", 5: "BA", 6: "CE", 7: "DF",
    8: "ES", 9: "GO", 10: "MA", 11: "MG", 12: "MS", 13: "MT", 14: "PA",
    15: "PB", 16: "PE", 17: "PI", 18: "PR", 19: "RJ", 20: "RN", 21: "RO",
    22: "RR", 23: "RS", 24: "SC", 25: "SE", 26: "SP", 27: "TO"
}

mapa_para_numerico = {sigla: numero for numero, sigla in mapa_localidades_correto.items()}

# 2. Carregar o arquivo com as siglas dos estados
try:
    df = pd.read_excel("DB_Definitivo.xlsx")
    print("--- DataFrame Original (com siglas) ---")
    print(df)

    # 3. Aplicar o mapa invertido para converter siglas em números
    # O .map() irá substituir cada sigla pelo número correspondente
    # Valores que não estão no mapa (como 'Sem localidade definida') se tornarão NaN
    df['Localidade(s)'] = df['Localidade(s)'].map(mapa_para_numerico)

    print("\n--- DataFrame Convertido (com códigos numéricos) ---")
    print(df)

    # 4. Salvar o resultado final
    df.to_excel("DB.xlsx", index=False)
    print("\nArquivo 'DB.xlsx' salvo com sucesso!")

except FileNotFoundError:
    print("Erro: Arquivo 'dados_localidades_padronizadas.xlsx' não encontrado.")
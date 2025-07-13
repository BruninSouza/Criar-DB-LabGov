import pandas as pd

# Criando coluna Grupos

try:
    # Carregar os arquivos XLSX
    df_a = pd.read_excel("arquivos-xslx/BD-Extensão.xlsx")
    df_b = pd.read_excel("arquivos-xslx/grupo-Analise-Licitacoes.xlsx")
    df_c = pd.read_excel("arquivos-xslx/grupo-outros.xlsx")

    # Criar a nova coluna 'Status' em A
    # e preencher com as cedulas com seus valores correspondentes 
    # para cada ID de A que também está em B ou C
    df_a.loc[df_a['ID'].isin(df_b['ID']), 'Grupo'] = 1
    df_a.loc[df_a['ID'].isin(df_c['ID']), 'Grupo'] = 3

    # Salvar o DataFrame A modificado em um novo arquivo XLSX
    df_a.to_excel("arquivos-xslx/DB.xlsx", index=False)

    print("O arquivo 'A_com_status.xlsx' foi criado com sucesso!")
    print("\nVisualização do arquivo modificado:")
    print(df_a)

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")

# Criando coluna Avaliação
try:
    df_a = pd.read_excel("arquivos-xslx/DB.xlsx")
    df_b = pd.read_excel("arquivos-xslx/avaliacao-nao.xlsx")
    df_c = pd.read_excel("arquivos-xslx/avaliacao-sim.xlsx")

    df_a.loc[df_a['ID'].isin(df_b['ID']), 'Avaliação'] = 0
    df_a.loc[df_a['ID'].isin(df_c['ID']), 'Avaliação'] = 1

    df_a.to_excel("arquivos-xslx/DB.xlsx", index=False)

    print("O arquivo 'A_com_status.xlsx' foi criado com sucesso!")
    print("\nVisualização do arquivo modificado:")
    print(df_a)

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")
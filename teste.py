import pandas as pd



# Carregar os arquivos XLSX
try:
    df_a = pd.read_excel("DB_com_grupo.xlsx")
    df_b = pd.read_excel("grupo-Analise-Licitacoes.xlsx")

    # Criar a nova coluna 'Status' em A
    # e preencher com 'OK' para cada ID de A que também está em B
    df_a.loc[df_a['ID'].isin(df_b['ID']), 'Grupo'] = 1

    # Salvar o DataFrame A modificado em um novo arquivo XLSX
    df_a.to_excel("DB_com_grupo.xlsx", index=False)

    print("O arquivo 'A_com_status.xlsx' foi criado com sucesso!")
    print("\nVisualização do arquivo modificado:")
    print(df_a)


except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")
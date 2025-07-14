import pandas as pd

# Criando coluna Grupos
try:
    # Carregar os arquivos XLSX
    df_a = pd.read_excel("arquivos-xlsx/BD-Extensão.xlsx")
    df_b = pd.read_excel("arquivos-xlsx/grupo-analise-licitacoes.xlsx")
    df_c = pd.read_excel("arquivos-xlsx/grupo_contratos_externos.xlsx")
    df_d = pd.read_excel("arquivos-xlsx/grupo-outros.xlsx")
    df_e = pd.read_excel("arquivos-xlsx/grupo_prestacao_contas.xlsx")
    df_f = pd.read_excel("arquivos-xlsx/grupo_demanda_externa.xlsx")
    
    # 1. Juntar todos os IDs dos outros DataFrames em uma única lista ou Série
    ids_conhecidos = pd.concat([df_b['ID'],df_c['ID'],df_d['ID'],df_e['ID'],df_f['ID']]).unique()

    # Criar a nova coluna 'Grupo'
    # e a preenche com as cedulas com seus valores correspondentes 
    # para cada ID de def_a que está presente nos outros datasets
    df_a.loc[df_a['ID'].isin(df_b['ID']), 'Grupo'] = 1
    df_a.loc[df_a['ID'].isin(df_c['ID']), 'Grupo'] = 2
    df_a.loc[df_a['ID'].isin(df_d['ID']), 'Grupo'] = 3
    df_a.loc[df_a['ID'].isin(df_e['ID']), 'Grupo'] = 5
    df_a.loc[df_a['ID'].isin(df_f['ID']), 'Grupo'] = 6

    # Isso atribui 99 (indefinido) a todos os IDs de df_a que NÃO estão na lista 'ids_conhecidos'
    df_a.loc[~df_a['ID'].isin(ids_conhecidos), 'Grupo'] = 99

    # Salvar o DataFrame A modificado em um novo arquivo XLSX
    df_a.to_excel("arquivos-xlsx/DB.xlsx", index=False)

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")
#####################################################################################################################

# Criando coluna Avaliação
try:
    df_a = pd.read_excel("arquivos-xlsx/DB.xlsx")
    df_b = pd.read_excel("arquivos-xlsx/avaliacao-nao.xlsx")
    df_c = pd.read_excel("arquivos-xlsx/avaliacao-sim.xlsx")

    df_a.loc[df_a['ID'].isin(df_b['ID']), 'Avaliação'] = 0
    df_a.loc[df_a['ID'].isin(df_c['ID']), 'Avaliação'] = 1

    df_a.to_excel("arquivos-xlsx/DB.xlsx", index=False)

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")
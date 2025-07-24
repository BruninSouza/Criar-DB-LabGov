import pandas as pd
import os

# Salvando caminho para os arquivos que serão lidos
script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

caminho_db_a = os.path.join(projeto_raiz, 'arquivos-xlsx', "BD-Combinado.xlsx")
caminho_db_b = os.path.join(projeto_raiz, 'arquivos-xlsx', "grupo_analise_licitacoes.xlsx")
caminho_db_c = os.path.join(projeto_raiz, 'arquivos-xlsx', "grupo_contratos_externos.xlsx")
caminho_db_d = os.path.join(projeto_raiz, 'arquivos-xlsx', "grupo_outros.xlsx")
caminho_db_e = os.path.join(projeto_raiz, 'arquivos-xlsx', "grupo_prestacao_contas.xlsx")
caminho_db_f = os.path.join(projeto_raiz, 'arquivos-xlsx', "grupo_demanda_externa.xlsx")

# Caminho do arquivo de saída
caminho_arquivo_saida = os.path.join(projeto_raiz, 'arquivos-xlsx', "BD-Combinado.xlsx")

# Criando coluna Grupos
try:
    # Carregar os arquivos XLSX
    df_a = pd.read_excel(caminho_db_a)
    df_b = pd.read_excel(caminho_db_b)
    df_c = pd.read_excel(caminho_db_c)
    df_d = pd.read_excel(caminho_db_d)
    df_e = pd.read_excel(caminho_db_e)
    df_f = pd.read_excel(caminho_db_f)
    
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
    df_a.to_excel(caminho_arquivo_saida, index=False)
    print("✅Coluna Grupo Criada com Sucesso!!")

except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")
#####################################################################################################################

# Salvando caminho para os arquivos que serão lidos
caminho_db_g = os.path.join(projeto_raiz, 'arquivos-xlsx', "BD-Combinado.xlsx")
caminho_db_h = os.path.join(projeto_raiz, 'arquivos-xlsx', "avaliacao-nao.xlsx")
caminho_db_i = os.path.join(projeto_raiz, 'arquivos-xlsx', "avaliacao-sim.xlsx")

# Criando coluna Avaliação
try:
    df_g = pd.read_excel(caminho_db_g)
    db_h = pd.read_excel(caminho_db_h)
    db_i = pd.read_excel(caminho_db_i)
    df_g.loc[df_g['ID'].isin(db_h['ID']), 'Avaliação'] = 0
    df_g.loc[df_g['ID'].isin(db_i['ID']), 'Avaliação'] = 1

    df_g.to_excel(caminho_arquivo_saida, index=False)
    print("✅Coluna Avaliação Criada com Sucesso!!")
except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os nomes dos arquivos estão corretos. Detalhes: {e}")
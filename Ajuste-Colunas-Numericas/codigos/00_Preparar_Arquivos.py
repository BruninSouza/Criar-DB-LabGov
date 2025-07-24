import pandas as pd
import os
import glob # Biblioteca para encontrar arquivos que correspondem a um padrão

script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir) 

caminho_padrao = os.path.join(projeto_raiz, 'arquivos-xlsx', "*.xlsx")
lista_arquivos_xlsx = glob.glob(caminho_padrao)

print("=== Iniciando preparação para formatar arquivos xlsx corretamente... ===")

# Verificando se existem arquivos na pasta especificada
if not lista_arquivos_xlsx:
    print("\nNenhum arquivo .xlsx foi encontrado no diretório especificado.")
else:
    print(f"\nEncontrados {len(lista_arquivos_xlsx)} arquivos. Iniciando verificação...")

# Atualizando nome da oluna "Número do Relatório" para ID
for caminho_arquivo in lista_arquivos_xlsx:
    try:
        nome_arquivo = os.path.basename(caminho_arquivo)
        df = pd.read_excel(caminho_arquivo)

        if 'Número do Relatório' in df.columns:
            df.rename(columns={'Número do Relatório': 'ID'}, inplace=True)
            df.to_excel(caminho_arquivo, index=False) # Salva o DataFrame modificado de volta no mesmo arquivo Excel

            print(f"✅ Coluna alterada com sucesso em: '{nome_arquivo}'")

        else:
            print(f"ℹ️ Coluna 'Número Relatório' não encontrada em: '{nome_arquivo}'. Nenhuma alteração feita.")

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo '{nome_arquivo}': {e}")

print("\nProcesso concluído!!")
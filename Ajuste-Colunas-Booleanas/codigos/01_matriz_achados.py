import csv
from pathlib import Path

print("=== Iniciando processo de gerar colunas com valores booleanos... ===\n")

# Salvando caminho para os arquivos que serão lidos
script_dir = Path(__file__).parent
projeto_raiz = script_dir.parent

# Nome do arquivo txt de entrada e do arquivo csv de saída
nome_arquivo_csv = "01_matriz_achados.csv"
arquivo_txt = projeto_raiz / "arquivos" / "resultado_matriz_achados.txt"
arquivo_csv = projeto_raiz /'csv-gerados' / nome_arquivo_csv

# Criar um conjunto para armazenar os números das linhas que contêm arquivos .pdf
linhas_com_pdf = set()

# Abrir o arquivo de texto e processar cada linha para encontrar as referências de arquivos .pdf
with open(arquivo_txt, 'r') as f:
    for linha in f:
        if '.pdf:' in linha:
            # Extraindo o número da linha antes de ".pdf"
            numero_linha = int(linha.split('.pdf:')[0])
            linhas_com_pdf.add(numero_linha)

# Criar o arquivo CSV com 343 linhas
with open(arquivo_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Matriz de Achados?'])  # Escrever o cabeçalho na primeira linha
    for i in range(1, 1 + 343):
        # Escrever 1 se o número da linha estiver no conjunto, caso contrário 0
        writer.writerow([1 if i in linhas_com_pdf else 0])

print(f"Arquivo '{nome_arquivo_csv}' gerado com sucesso!")
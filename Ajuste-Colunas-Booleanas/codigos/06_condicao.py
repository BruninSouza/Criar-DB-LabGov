import csv
from pathlib import Path

script_dir = Path(__file__).parent
projeto_raiz = script_dir.parent

nome_arquivo_csv = "06_condicao.csv"

arquivo_txt = projeto_raiz / 'arquivos' / 'resultado_condicao.txt'
arquivo_csv = projeto_raiz / 'csv-gerados' / nome_arquivo_csv

linhas_com_pdf = set()

with open(arquivo_txt, 'r') as f:
    for linha in f:
        if '.pdf:' in linha:
            numero_linha = int(linha.split('.pdf:')[0])
            linhas_com_pdf.add(numero_linha)

with open(arquivo_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['e. Condição ou situação encontrada (O que é) [achados]'])
    for i in range(1, 1 + 343):
        writer.writerow([1 if i in linhas_com_pdf else 0])

print(f"Arquivo '{nome_arquivo_csv}' gerado com sucesso!")
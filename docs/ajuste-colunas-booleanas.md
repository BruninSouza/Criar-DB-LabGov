# **Módulo de Ajuste de Colunas Booleanas**

O módulo **Ajuste de Colunas Booleanas** é fundamental para garantir a consistência de dados que representam estados binários (como "Presente/Faltando" e "Sim/Não). Ele automatiza a leitura, filtragem, normalização e combinação dessas colunas.

---

## **Como Funciona**

Os scripts  deste módulo (localizados em `Ajuste-Colunas-Booleanas/codigos/`), são divididos em dois tipos de scripts, cada um realiza uma etapa do processos distintos, são eles:

### **Scripts de criação de colunas**

Os scripts Python (`.py`) enumerados de 01 à 15 localizados em `Atualizar-Dataset/codigos/` orquestram as seguintes ações:

1.  **Leitura do Arquivo de Texto**: O script abre um arquivo de texto específico (definido como `nome_do_arquivo` no exemplo, mas que deve ser substituído pelo caminho real do arquivo TXT contendo as referências).
2.  **Identificação de Linhas com PDF**: Percorre cada linha do arquivo de texto em busca da string `.pdf:`. Se a string for encontrada, o número da linha (que precede `.pdf:`) é extraído e armazenado.
3.  **Criação do Arquivo CSV de Saída**: Um novo arquivo CSV é criado (definido como `00_nome_coluna.csv` no exemplo, mas pode ser qualquer nome, entretando, é indicado que possuam um indice no inicio do nome, pois durante a criação do dataset as colunas são ordenadas em ordem alfabética).
4.  **Escrita do Cabeçalho**: A primeira linha do CSV é definida com o nome da coluna, conforme especificado no script (`Nome da coluna`).
5.  **Preenchimento da Coluna Booleana**: O script itera por um número predefinido de linhas (atualmente 343, mas configurável). Para cada linha, ele verifica se o número da linha corresponde a uma das linhas que continham a referência `.pdf` no arquivo de texto original.
    * Se houver correspondência, o valor `1` (verdadeiro) é escrito na linha do CSV.
    * Caso contrário, o valor `0` (falso) é escrito.
6.  **Confirmação**: Uma mensagem é exibida confirmando a geração bem-sucedida do arquivo CSV.

#### **Exemplo de Código:** `cria_coluna_booleana.py`

A seguir, o código completo do script `Ajuste-Colunas-Booleanas/codigos/01_matriz_achados.py` exemplifica a lógica implementada nos scripts de criação de colunas booleanas:

```python

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

```

### **Script de junção de colunas num só banco de dados**

O script `16_juntar-colunas.py` localizados em `Atualizar-Dataset/codigos/`, orquestra as seguintes ações:

1.  **Listagem e Ordenação de Arquivos**: O script primeiro encontra todos os arquivos CSV presentes na pasta `csv-gerados/` (que é onde os CSVs individuais de colunas booleanas são gerados). Ele então **ordena esses arquivos alfabeticamente** para garantir uma ordem consistente na combinação.
2.  **Leitura dos Arquivos CSV**: Cada arquivo CSV encontrado é lido e transformado em um DataFrame do Pandas.
3.  **Combinação de DataFrames**: Todos os DataFrames individuais são unidos **lado a lado (por colunas)** em um único DataFrame grande.
4.  **Salvamento em XLSX**: O DataFrame combinado é salvo em um novo arquivo XLSX chamado `colunas_combinadas.xlsx` na raiz do módulo (`Ajuste-Colunas-Booleanas/`).
6.  **Confirmação**: Uma mensagem é exibida no console confirmando que os arquivos foram combinados e convertidos com sucesso.

#### **Exemplo de Código:** `16_juntar-colunas.py`

A seguir, o código completo do script `Ajuste-Colunas-Booleanas/codigos/16_juntar-colunas.py`, que demonstra a lógica de combinação de múltiplos arquivos CSV na criação de um banco de dados.

```python
import pandas as pd 
import glob

# Lista todos os arquivos CSV na pasta csv-gerados e ordena alfabeticamente
caminho_arquivos = sorted(glob.glob("csv-gerados/*.csv"))

# Lista para armazenar cada DataFrame
dataframes = []

# Itera sobre cada arquivo CSV ordenado e adiciona ao dataframe
for arquivo in caminho_arquivos:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

# Junta todos os DataFrames por colunas
df_combined = pd.concat(dataframes, axis=1)

# Salva o DataFrame combinado em um novo arquivo XLSX
df_combined.to_excel("./dataframe.xlsx", index=False)

print("Arquivos combinados com sucesso em ordem alfabética e convertidos para XLSX!")
```
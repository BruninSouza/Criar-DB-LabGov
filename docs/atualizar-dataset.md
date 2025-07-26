# **Módulo de Atualização do Dataset Principal**

O módulo **Atualizar Dataset** é a fase final e crucial do nosso pipeline de automação. Ele é responsável por integrar e consolidar todos os dados processados, combinando informações numéricas e booleanas em um novo banco de dados, e então atualizando o dataset principal do projeto. Este processo garante que suas análises e relatórios sejam sempre baseados nas informações mais recentes e abrangentes

---

## **Como Funciona**

A pasta `Atualizar-Dataset/codigos/` possuí dois scripts, o primeiro cria um novo banco de dados com todos os dados processados até então, e o segundo atualiza o dataset principal do projeto com os novos dados coletados. A seguir uma explicação mais aprofundada a cerca dos scripts: 

### **Criar dataset com dados novos**

O script `01_Criar_DB.py`, localizado em `Atualizar-Dataset/codigos/`, orquestra as seguintes ações:

1.  **Definição de Caminhos**: O script primeiro define os caminhos para os arquivos de entrada e saída. Ele busca:
    - `DB.xlsx`: O dataset contendo colunas numéricas combinadas (gerado pelo módulo de Ajuste de Colunas Numéricas).
    - `colunas_combinadas.xlsx`: O dataset contendo colunas booleanas combinadas (gerado pelo módulo de Ajuste de Colunas Booleanas).
    - O arquivo de saída `DB_novo.csv` será gerado dentro da pasta `Atualizar-Dataset/datasets/`.
2.  **Carregamento dos DataFrames:**: Os arquivos `DB.xlsx` e `colunas_combinadas.xlsx` são lidos e carregados como DataFrames do Pandas.
3.  **Concatenação por Colunas**: Os dois DataFrames são c**oncatenados lado a lado** (ou seja, por colunas). Isso significa que as colunas do dataset numérico e as colunas do dataset booleano são unidas para formar um único DataFrame abrangente.
4.  **Salvamento do Novo Dataset**: O DataFrame combinado resultante é salvo em um novo arquivo CSV chamado `DB_novo.csv` no diretório `Atualizar-Dataset/datasets/`.
5.  **Confirmação**: Uma mensagem de sucesso é exibida no console, indicando que o novo banco de dados foi gerado com êxito. Em caso de qualquer problema durante o processo, uma mensagem de erro será exibida.


#### **Exemplo de Código:** `01_Criar_DB.py`

A seguir, o código completo do script `Atualizar-Dataset/codigos/01_Criar_DB.py`, que ilustra a lógica de união dos datasets.

```python
import pandas as pd
from pathlib import Path
import os # Necessário para criar diretórios se não existirem

# Obtém o diretório do script atual e a raiz do projeto
script_dir = Path(__file__).parent.parent
projeto_raiz = script_dir.parent

# Define os caminhos completos para os arquivos de entrada
caminho_db_a = projeto_raiz / 'Ajuste-Colunas-Numericas' / "DB.xlsx"
caminho_db_b = projeto_raiz / 'Ajuste-Colunas-Booleanas' / "colunas_combinadas.xlsx"

# Define o caminho completo para o arquivo CSV de saída
# Ele será salvo dentro da pasta 'datasets' do módulo 'Atualizar-Dataset'
caminho_pasta_saida = script_dir / "datasets"
caminho_arquivo_saida_csv = script_dir / "datasets" /"DB_novo.csv"

# Garante que o diretório de saída exista
os.makedirs(caminho_pasta_saida, exist_ok=True)

try:
    print("=== Juntando Colunas Numericas e Booleanas num só DB.... ===")

    # Carrega os DataFrames dos arquivos XLSX
    db_a = pd.read_excel(caminho_db_a)
    db_b = pd.read_excel(caminho_db_b)

    # Lista de DataFrames a serem combinados
    dataframes = [db_a, db_b]

    # Concatena os DataFrames por colunas (lado a lado)
    # Assumimos que as linhas se alinham ou que a ordem é garantida pelos processos anteriores.
    # Se houver necessidade de merge por chaves (ID, etc.), a lógica aqui seria diferente (pd.merge).
    df_combined = pd.concat(dataframes, axis=1)

    # Salvando em csv
    df_combined.to_csv(caminho_arquivo_saida_csv, index=False)

    print("✅Novo Banco de Dados Gerado com Sucesso!!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

### **Atualizar dataset antigo com dados novos**

O script `02_Atualizar_DB.py`, localizado em `Atualizar-Dataset/codigos/`, executa as seguintes ações:

1.  **Definição de Caminhos**: O script primeiro define os caminhos para os arquivos de entrada e saída. Ele busca:
    - `relatorios.csv`: O dataset "antigo" ou base, localizado em `Atualizar-Dataset/datasets/`.
    - `DB_novo.csv`: O dataset "novo", que contém as informações mais recentes (gerado pelo passo anterior), também localizado em `Atualizar-Dataset/datasets/`.
    - Os arquivos de saída finais, `Dataset.xlsx` e `relatorios.csv`, serão gerados na raiz do projeto.
2.  **Carregamento dos DataFrames:**: Os arquivos `relatorios.csv` e `DB_novo.csv` são lidos e carregados como DataFrames do Pandas (`df_a` e `df_b`, respectivamente).
3.  **Remoção de Colunas Específicas:**: O script **remove as colunas 'Ação' e 'Filtro'** do dataset `relatorios.csv` (`df_a`). Essa etapa é crucial para padronizar o dataset antigo antes da concatenação.
4. **Concatenação Vertical dos DataFrames**: Os dois DataFrames (`df_a` modificado e `df_b`) são **concatenados verticalmente**, ou seja, as linhas de `df_b` são adicionadas abaixo das linhas de `df_a`. O `ignore_index=True` garante que o índice do novo DataFrame seja reiniciado.
5.  **Salvamento dos Datasets Finais**: O DataFrame final combinado (`df_final`) é salvo em dois formatos diferentes na raiz do projeto:
    - `Dataset.xlsx`: Uma versão em Excel.
    - `relatorios.csv`: Uma versão em CSV, ideal para análises e relatórios.
6.  **Confirmação**: Uma mensagem de sucesso é exibida no console, confirmando que o banco de dados foi atualizado com êxito.

#### **Exemplo de Código:** `02_Atualizar_DB.py`

A seguir, o código completo do script `Atualizar-Dataset/codigos/02_Atualizar_DB.py`, que ilustra a lógica de união e remoção de colunas.

```python
import pandas as pd
from pathlib import Path

# Define os caminhos do script e da raiz do projeto
script_dir = Path(__file__).parent.parent
projeto_raiz = script_dir.parent

# Define os caminhos para os arquivos de entrada (dentro da pasta 'datasets' do módulo)
caminho_db_a = script_dir / "datasets" / "relatorios.csv" # Dataset antigo/base
caminho_db_b = script_dir / "datasets" / "DB_novo.csv"    # Dataset novo, gerado no passo anterior

# Define os caminhos para os arquivos de saída (na raiz do projeto)
arquivo_saida_xlsx = projeto_raiz / "Dataset.xlsx"
arquivo_saida_csv = projeto_raiz / "relatorios.csv"

try:
    print("=== Carregando datasets para atualização... ===")
    df_a = pd.read_csv(caminho_db_a)
    df_b = pd.read_csv(caminho_db_b)

    print(f"Dataset 'relatorios.csv' (antigo) carregado com {len(df_a.columns)} colunas e {len(df_a)} linhas.")
    print(f"Dataset 'DB_novo.csv' (novo) carregado com {len(df_b.columns)} colunas e {len(df_b)} linhas.")

    # Remove colunas específicas do dataset antigo
    # O 'inplace=True' modifica o DataFrame diretamente sem retornar uma cópia
    print("Removendo colunas 'Ação' e 'Filtro' do dataset antigo...")
    df_a.drop(columns=['Ação',"Filtro"], inplace=True) 
    print(f"Colunas restantes no dataset antigo: {len(df_a.columns)}")

    # Agora o df_a já não tem mais as colunas "Ação" e "Filtro"
    print("\n=== Concatenando Banco de Dados antigo com o novo... ===")
    
    # Concatena os DataFrames verticalmente (empilhando as linhas)
    # ignore_index=True redefine o índice do DataFrame final
    df_final = pd.concat([df_a, df_b], ignore_index=True)
    print(f"Concatenação concluída. O DataFrame final possui {len(df_final)} linhas e {len(df_final.columns)} colunas.")

    # Salvando o DataFrame final em formato XLSX
    print(f"Salvando o Banco de Dados atualizado em '{arquivo_saida_xlsx}'...")
    df_final.to_excel(arquivo_saida_xlsx, index=False)

    # Salvando o DataFrame final em formato CSV
    print(f"Salvando o Banco de Dados atualizado em '{arquivo_saida_csv}'...")
    df_final.to_csv(arquivo_saida_csv, index=False)

    print("✅ Banco de dados Atualizado com Sucesso!!")

except FileNotFoundError as e:
    print(f"Erro: Um dos arquivos de entrada não foi encontrado. Verifique se eles existem nos caminhos esperados: {e}")
except KeyError as e:
    print(f"Erro: Uma das colunas a serem removidas não foi encontrada no dataset antigo: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado durante a atualização do banco de dados: {e}")
```
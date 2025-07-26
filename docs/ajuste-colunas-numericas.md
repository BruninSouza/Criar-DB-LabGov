# **Módulo de Ajuste de Colunas Numéricas**

O módulo **Ajuste de Colunas Numéricas** é crucial para consolidar dados quantitativos de diversas fontes. Ele lida com a leitura de arquivos, a conversão de formatos e a combinação de colunas numéricas, garantindo que os dados estejam prontos para cálculos e análises.

---

## **Como Funciona**

O módulo Ajuste de Colunas Numéricas é executado em três fases distintas para garantir a correta preparação dos dados:

### **1. Padronização da Coluna 'ID'**

A primeira etapa, executada pelo script `00_Preparar_Arquivos.py`, foca em garantir que a coluna identificadora principal em todos os arquivos de entrada tenha um nome consistente. Ele realiza os seguintes processos:

1.  **Localização de Arquivos**: O script procura por todos os arquivos `.xlsx` dentro do diretório `Ajuste-Colunas-Numericas/arquivos-xlsx/`.
2.  **Processamento Individual**: Para cada arquivo Excel encontrado, ele o abre e verifica a existência da coluna 'Número do Relatório'.
3.  **Renomeação da Coluna**: Se a coluna 'Número do Relatório' for encontrada, ela é automaticamente renomeada para 'ID'. Essa padronização é vital para que os datasets possam ser combinados corretamente nas etapas futuras.
4.  **Salvamento das Alterações**: O arquivo Excel modificado é salvo de volta no mesmo local, sobrescrevendo a versão original com a coluna 'ID' renomeada.
6.  **Feedback**: Uma mensagem informativa é exibida para cada arquivo, indicando se a coluna foi alterada ou se não foi encontrada.

#### **Exemplo de Código:** `00_Preparar_Arquivos.py`

A seguir, o código responsável pela padronização da coluna 'ID':

```python 
import pandas as pd
import os
import glob # Biblioteca para encontrar arquivos que correspondem a um padrão

# Define os caminhos do script e da raiz do projeto
script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir) 

# Caminho para os arquivos XLSX brutos
caminho_padrao = os.path.join(projeto_raiz, 'Ajuste-Colunas-Numericas', 'arquivos-xlsx', "*.xlsx")
lista_arquivos_xlsx = glob.glob(caminho_padrao)

print("=== Iniciando preparação para formatar arquivos xlsx corretamente (Padronização de ID)... ===")

# Verificando se existem arquivos na pasta especificada
if not lista_arquivos_xlsx:
    print("\nNenhum arquivo .xlsx foi encontrado no diretório especificado em 'Ajuste-Colunas-Numericas/arquivos-xlsx/'.")
else:
    print(f"\nEncontrados {len(lista_arquivos_xlsx)} arquivos. Iniciando verificação e alteração...")

# Atualizando nome da coluna "Número do Relatório" para "ID"
for caminho_arquivo in lista_arquivos_xlsx:
    try:
        nome_arquivo = os.path.basename(caminho_arquivo)
        df = pd.read_excel(caminho_arquivo)

        if 'Número do Relatório' in df.columns:
            df.rename(columns={'Número do Relatório': 'ID'}, inplace=True)
            df.to_excel(caminho_arquivo, index=False) # Salva o DataFrame modificado de volta no mesmo arquivo Excel

            print(f"✅ Coluna 'Número do Relatório' alterada para 'ID' com sucesso em: '{nome_arquivo}'")

        else:
            print(f"ℹ️ Coluna 'Número do Relatório' não encontrada em: '{nome_arquivo}'. Nenhuma alteração feita na coluna ID.")

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo '{nome_arquivo}': {e}")

print("\nProcesso de Padronização de ID concluído!!")
```

### **2. Leitura, Processamento e Combinação de Colunas Numéricas**

Após a padronização dos IDs, os próximos scripts (dos enumerados 01 até 04) se encarregam da manipulação dos dados numéricos.

1. **Leitura de Arquivos XLSX**: Lê os arquivos de dados brutos do diretório `Ajuste-Colunas-Numericas/arquivos-xlsx/` (agora com a coluna 'ID' padronizada).

2. **Extração e Limpeza**: Identifica as colunas numéricas relevantes, remove caracteres não numéricos e trata valores ausentes (NaN).

3. **Conversão de Tipo**: Garante que os dados sejam convertidos para tipos numéricos apropriados (inteiros).

4. **Combinação**: Mescla as colunas numéricas processadas em um único DataFrame consolidado.

5. **Geração do Dataset Final**: O DataFrame final é salvo como `DB.xlsx` na raiz do módulo (`Ajuste-Colunas-Numericas/`).

#### **Exemplo de Código:** `01_Criar_Coluna_Servico`

A seguir, um exemplo de como o código para a geração de colunas numéricas, como a transformação da coluna "Serviço", pode ser estruturado.

```python
import pandas as pd
import os

# Define os caminhos do script e da raiz do projeto
script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir) # Sobe um nível para a raiz do projeto

# Define os caminhos completos para os arquivos de entrada e saída
# 'BD-Extensão.xlsx' é o arquivo original de onde os dados de serviço serão lidos.
caminho_db_entrada = os.path.join(projeto_raiz, 'Ajuste-Colunas-Numericas', 'arquivos-xlsx', "BD-Extensão.xlsx")

# 'BD-Combinado.xlsx' é o arquivo de saída com a coluna 'Serviço' padronizada para números.
caminho_arquivo_saida = os.path.join(projeto_raiz, 'Ajuste-Colunas-Numericas', 'arquivos-xlsx', "BD-Combinado.xlsx")

# Mapeamento dos nomes de serviço para siglas e, em seguida, para números.
# Isso permite que os valores textuais da coluna "Serviço" sejam convertidos em códigos numéricos.
MAPA_NOME_PARA_SIGLA = {1: "Avaliação", 2: "Consultoria", 3: "Apuração"}
mapa_para_numerico = {sigla: numero for numero, sigla in MAPA_NOME_PARA_SIGLA.items()}

try:
    print("\n=== Iniciando processo de gerar dataset com valores numéricos... ===")
    
    # Carrega o DataFrame do arquivo Excel de entrada
    df_entrada = pd.read_excel(caminho_db_entrada)
    
    # Exibe as colunas antes da transformação para depuração
    print(f"Colunas do DataFrame de entrada: {df_entrada.columns.tolist()}")

    # Verifica se a coluna "Serviço" existe antes de tentar mapear
    if "Serviço" in df_entrada.columns:

        # Aplica o mapeamento para converter os nomes de serviço em números
        df_entrada["Serviço"] = df_entrada["Serviço"].map(mapa_para_numerico)

        # Tratar valores que não foram mapeados (NaN após o .map())
        df_entrada["Serviço"] = df_entrada["Serviço"].fillna(99)
        
        # Salva o DataFrame modificado no arquivo de saída
        df_entrada.to_excel(caminho_arquivo_saida, index=False)
        print("✅ Coluna 'Serviço' Atualizada com Sucesso para valores numéricos!!")

    else:
        print(f"ℹ️ Coluna 'Serviço' não encontrada no arquivo '{os.path.basename(caminho_db_entrada)}'. Nenhuma alteração de serviço feita.")

        # Se a coluna não for encontrada, ainda podemos salvar o arquivo de entrada para a próxima etapa
        df_entrada.to_excel(caminho_arquivo_saida, index=False)

        print(f"Arquivo '{os.path.basename(caminho_db_entrada)}' salvo como '{os.path.basename(caminho_arquivo_saida)}' sem modificação na coluna 'Serviço'.")

except FileNotFoundError as e:
    print(f"Erro: Arquivo '{os.path.basename(caminho_db_entrada)}' não encontrado. Verifique se o caminho e o nome do arquivo estão corretos. Detalhes: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado durante o processamento da coluna numérica 'Serviço': {e}")

print("\nProcesso de geração de dataset com valores numéricos concluído!!")
```

### **3. Renomeação e Organização Final das Colunas**

Esta é a etapa final de preparação dentro do módulo numérico, onde as colunas recebem seus nomes definitivos e são reordenadas para um layout padronizado.

1. **Carregamento do Dataset**: O script lê o arquivo `DB.xlsx `(gerado pelas etapas anteriores, com a coluna 'ID' padronizada e 'Serviço' numérica).

2. **Renomeação de Colunas**: As colunas são renomeadas de acordo com as necessidades do projeto. Especificamente, "Título" torna-se "Nome" e "Publicação" torna-se "Data".

3. **Definição da Ordem das Colunas**: Uma lista predefinida (`colunas_organizadas`) especifica a ordem final desejada para as colunas no dataset.

4. **Reordenação do DataFrame**: O DataFrame é reordenado para corresponder à sequência definida em `colunas_organizadas`, garantindo que o dataset final tenha uma estrutura consistente.

5. **Salvamento do Dataset Organizado**: O DataFrame com as colunas renomeadas e organizadas é salvo de volta no arquivo `DB.xlsx`, sobrescrevendo a versão anterior.

6. **Confirmação**: Uma mensagem de sucesso é exibida confirmando que as colunas foram renomeadas e organizadas corretamente.

#### **Exemplo de Código:** `05_Organizando_Colunas.py`

Este é o código que realiza a etapa de renomeação e organização das colunas:

```python
import pandas as pd
import os

# Define os caminhos do script e da raiz do projeto
script_dir = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(script_dir)

# O caminho_arquivo refere-se ao DB.xlsx final que foi gerado nas etapas anteriores.
caminho_arquivo = os.path.join(projeto_raiz, "DB.xlsx")

try:
    # Carrega o DataFrame do arquivo DB.xlsx
    df = pd.read_excel(caminho_arquivo)

    # Renomeando Colunas para nomes adequados
    df_renomeado = df.rename(columns={"Título": "Nome", "Publicação": "Data"})

    # Define a ordem correta e as colunas esperadas no dataset final
    colunas_organizadas = ["ID", "Nome", "Serviço", "Grupo", "Avaliação", "Data", "Ano", "Governo", "UF"]
    
    # Verifica se todas as colunas esperadas estão presentes após a renomeação
    colunas_faltando = [col for col in colunas_organizadas if col not in df_renomeado.columns]    
    if colunas_faltando:
        print(f"Atenção: As seguintes colunas esperadas não foram encontradas no DataFrame: {colunas_faltando}. Elas podem aparecer como NaN no resultado final.")

    # Seleciona e reordena as colunas. Colunas não listadas serão descartadas.
    # Usamos .loc para garantir que a seleção de colunas seja feita de forma segura.
    df_copy = df_renomeado
    df_copy = df_copy[colunas_organizadas]

    # Salva o DataFrame com as colunas renomeadas e organizadas de volta no mesmo arquivo Excel
    df_copy.to_excel(caminho_arquivo, index=False)

    print("✅Colunas Renomeadas e Organizadas com Sucesso!!")

except FileNotFoundError as e:
    print(f"Erro: Arquivo '{os.path.basename(caminho_arquivo)}' não encontrado. Verifique se o caminho e o nome do arquivo estão corretos. Detalhes: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado durante a renomeação e organização das colunas: {e}")
```
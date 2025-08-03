# **Preparação dos Dados para Execução do Projeto**

Para que os módulos de automação funcionem corretamente, é essencial que os arquivos de dados estejam organizados e nomeados conforme as especificações. Siga as instruções abaixo para preparar seu ambiente.

## **1. Módulo de Ajuste de Colunas Numéricas**

Este módulo requer arquivos de dados específicos baixados do site da CGU (Controladoria-Geral da União).

### **A. Download dos Arquivos XLSX**

1. Acesse o site da CGU através do [link](https://eaud.cgu.gov.br/relatorios/pesquisa).

2. Baixe os seguintes arquivos XLSX, filtrando pelo período de tempo especificado que você deseja analisar:

    - **Arquivo Normal**: Um arquivo XLSX com o filtro do período de tempo. Este será o arquivo base.

    - **Arquivo de Grupos**: Um arquivo XLSX no mesmo período de tempo, mas com filtros específicos para "grupos".

    - **Arquivo de Avaliação**: Um arquivo XLSX no mesmo período de tempo, mas com filtros específicos para "avaliação".

3. Nomeação dos Arquivos: É crucial que o nome desses arquivos siga um padrão específico para que os scripts consigam lê-los corretamente. Certifique-se de nomeá-los de forma consistente, como por exemplo:

    - `BD-Extensão.xslx`: para o arquivo base.

    - `grupo_nome_do_grupo.xlsx`: para os arquivos filtrados por grupo

    - `avaliacao_sim.xslx` e `avaliacao_nao.xlsx`: para os arquivos filtrados por avaliacao (só existem sim e não)
        
>⚠️Importante: Os nomes exatos devem ser compatíveis com a lógica de leitura dos seus scripts Python. Se seu script espera nomes muito específicos como BD-Extensão.xlsx, use esses nomes.

### **B. Organização dos Arquivos**

- **Limpe a Pasta Existente**: Antes de mover os novos arquivos, remova todos os arquivos .xlsx que estão atualmente no diretório: `Ajuste-Colunas-Numericas/arquivos-xlsx/`

- **Mova os Novos Arquivos**: Copie os arquivos XLSX que você acabou de baixar e nomear para o diretório: `Ajuste-Colunas-Numericas/arquivos-xlsx/`

## **2. Módulo de Ajuste de Colunas Booleanas**

Este módulo utiliza arquivos de texto (`.txt`) gerados a partir de uma metodologia anterior (provavelmente a que identifica referências a PDFs).

### **A. Obtenção dos Arquivos .txt**

- Recupere os arquivos `.txt` criados usando a metodologia descrita anteriormente para a geração de colunas booleanas.

A metodologia de Geração dos arquivos `.txt` se encontra no [Link](https://docs.google.com/document/d/1SqfNRUad_ccG6rAjSugxbDS6db2O_lf-TVVCaA3C6TM/edit?usp=sharing).

### **B. Organização dos Arquivos**

- **Limpe a Pasta Existente**: Remova todos os arquivos `.txt` que estão atualmente no diretório: `Ajuste-Colunas-Booleanas/arquivos/`

- **Mova os Novos Arquivos**: Copie os arquivos `.txt` recuperados para o diretório: `Ajuste-Colunas-Booleanas/arquivos/`

## **3. Módulo de Atualizar Dataset**

Para este módulo, você precisará fornecer a versão mais recente do seu arquivo de relatórios para que ele seja atualizado com os novos dados processados.

### **A. Obtenção do Arquivo relatorios.csv**

Localize o arquivo `relatorios.csv` que está sendo atualmente utilizado para suas análises de relatórios. Este é o dataset base que será atualizado.

### **B. Organização do Arquivo**

- **Limpe a Pasta Existente**: Remova o arquivo relatorios.csv que está atualmente no diretório: `Atualizar-Dataset/datasets/`

- **Mova o Novo Arquivo**: Copie a versão mais recente do seu relatorios.csv para o diretório: `Atualizar-Dataset/datasets/`
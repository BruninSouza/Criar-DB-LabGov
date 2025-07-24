## 🗂️ Estrutura do Projeto

# Criação do Banco de Dados

#### UFPB - Universidade Federal da Paraíba
#### LabGov

Autor: Bruno Souza da Costa  
Contatos: [e-mail](brun.souz4@gmail.com) | [linkedin](https://www.linkedin.com/in/bruno-souza-a74396214/)

### Esse código foi utilizado para automatizar a criação do banco de dados do projeto "Relatórios de Auditorias Governamentais"

A metodologia completa utilizada para a criação do banco de dados se encontra no [link](https://docs.google.com/document/d/1SqfNRUad_ccG6rAjSugxbDS6db2O_lf-TVVCaA3C6TM/edit?usp=sharing).

A análise dos relatórios de auditoria interna governamental se encontra no [link](https://github.com/BruninSouza/relatorios_auditoria_interna_governamental?tab=readme-ov-file).


```bash
├── Ajuste-Colunas-Booleanas/     # Pasta onde os dataset com valores booleanos é criado
|    ├── arquivos/                # Pasta onde os arquivos criados por filtros estão inseridos
|    ├── codigos/                 # Pasta onde os códigos de automação estão inseridos
|    ├── csv-gerados/             # Pasta onde são inseridos os arquivos csv gerados pelos códigos de automação
|    └── colunas_combinadas.xslx  # Dataset contendo colunas de valores booleanos combinadas gerado automaticamente
|
├── Ajuste-Colunas-Numericas/     # Pasta onde os dataset com valores númericos é criado
|    ├── arquivos-xlsx/           # Pasta contendo arquivos baixados que serão convertidos em colunas
|    ├── codigos/                 # Pasta onde os códigos de automação estão inseridos 
|    └── DB.xslx                  # Dataset contendo colunas de valores númericos combinadas gerado automaticamente
|
├── Atualizar-Dataset/            # Pasta onde é o dataset antigo é atualizado com novos valores
|    ├── codigos/                 # Pasta contendo códigos que geram o novo dataset e atualizam o antigo
|    └── datasets/                # Pasta onde estão se localiza os datasets antigo e novo
|
├── .gitignore                    # Controla arquivos e diretorios que podem ser versionados
├── Dataset.xslx                  # Dataset xslx atualizado gerado automaticamente
├── README.md                     # Este arquivo
├── relatorios.csv                # Dataset csv atualizado gerado automaticamente que será usado para análises
├── requirements.txt              # Contém todas as bibliotecas python necessárias para funcionamento
└── script_main.sh                # Script responsável por gerar datasets atualizados automaticamente
```

## 🧪 Requisitos

- Sistema operacional Linux
- python 3.x instalado

## Como Usar

Clone este repositório:

```bash
git clone https://github.com/BruninSouza/Ajuste-Colunas.git
```
Abra-o na IDE de sua escolha e execute no terminal:

```bash
chmod +x script_main.sh
```

Issa dará permissão de execução para o arquivo de script, após isso execute novamente no terminal:

```bash
./script_main.sh
```
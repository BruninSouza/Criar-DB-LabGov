# **Atualizar Banco de Dados do LabGov**

#### **UFPB - Universidade Federal da Paraíba**
#### **LabGov**

Autor: Bruno Souza da Costa  
Contatos: [e-mail](brun.souz4@gmail.com) | [linkedin](https://www.linkedin.com/in/bruno-souza-a74396214/)

### **Esse código foi utilizado para automatizar a atualização do banco de dados usado no projeto "Relatórios de Auditorias Governamentais"**

A documentação completa utilizada para a criação deste projeto se encontra no [link](https://bruninsouza.github.io/Criar-DB-LabGov/).

A análise dos relatórios de auditoria interna governamental se encontra no [link](https://github.com/BruninSouza/relatorios_auditoria_interna_governamental?tab=readme-ov-file).

## 🎯 **Objetivos**

No mundo da análise de dados, a qualidade e a consistência das informações são cruciais. Este projeto resolve os desafios comuns de:

* **Padronização de Dados**: Garante que valores booleanos e numéricos estejam sempre no formato correto.
* **Automação**: Reduz a necessidade de intervenção manual, economizando tempo e minimizando erros.
* **Confiabilidade**: Fornece dataset atualizado e prontos para uso.

## 🗂️ **Estrutura do Projeto**

```bash
├── .github/                         # Contém configurações para GitHub Actions
|    └── workflows/
|        └── deploy-docs.yml         # Workflow para deploy automático da documentação
|
├── Ajuste-Colunas-Booleanas/        # Pasta onde os dataset com valores booleanos é criado
|    ├── arquivos/                   # Pasta onde os arquivos criados por filtros estão inseridos
|    ├── codigos/                    # Pasta onde os códigos de automação estão inseridos
|    ├── csv-gerados/                # Pasta onde são inseridos os arquivos csv gerados pelos códigos de automação
|    └── colunas_combinadas.xslx     # Dataset contendo colunas de valores booleanos combinadas gerado automaticamente
|
├── Ajuste-Colunas-Numericas/        # Pasta onde os dataset com valores númericos é criado
|    ├── arquivos-xlsx/              # Pasta contendo arquivos baixados que serão convertidos em colunas
|    ├── codigos/                    # Pasta onde os códigos de automação estão inseridos 
|    └── DB.xslx                     # Dataset contendo colunas de valores númericos combinadas gerado automaticamente
|
├── Atualizar-Dataset/               # Pasta onde é o dataset antigo é atualizado com novos valores
|    ├── codigos/                    # Pasta contendo códigos que geram o novo dataset e atualizam o antigo
|    └── datasets/                   # Pasta onde estão se localiza os datasets antigo e novo
|
├── docs/                            # pasta da documentação mkdocs
|    ├── index.md                    # Página inicial da documentação
|    ├── ajuste-colunas-booleanas.md # Documentação do módulo de booleanos
|    ├── ajuste-colunas-numericas.md # Documentação do módulo de numéricos
|    ├── atualizar-dataset.md        # Documentação do módulo de atualização
|    ├── como-executar.md            # Guia de execução do projeto
|    └── preparacao-dados.md         # Guia de preparação dos dados
|
├── .gitignore                       # Controla arquivos e diretorios que podem ser versionados
├── Dataset.xslx                     # Dataset xslx atualizado gerado automaticamente
├── mkdocs.yml                       # Arquivo de configuração do documentaçao
├── README.md                        # Este arquivo
├── relatorios.csv                   # Dataset csv atualizado gerado automaticamente que será usado para análises
├── requirements.txt                 # Contém todas as bibliotecas python necessárias para funcionamento
└── script_main.sh                   # Script responsável por gerar datasets atualizados automaticamente
```
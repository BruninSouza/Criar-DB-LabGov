# Criação e ajustes das colunas para o banco de dados 

#### UFPB - Universidade Federal da Paraíba
#### LabGov

Autor: Bruno Souza da Costa  
Contatos: [e-mail](brun.souz4@gmail.com) | [linkedin](https://www.linkedin.com/in/bruno-souza-a74396214/)

### Esse código foi utilizado para automatizar a criação das colunas Avaliação e Grupo, juntamente com a transformação da coluna localidade(s) em UF usando códigos numéricos invés de  strings

A metodologia completa utilizada para a criação dessas colunas pode ser encontrada no [link](https://docs.google.com/document/d/1SqfNRUad_ccG6rAjSugxbDS6db2O_lf-TVVCaA3C6TM/edit?usp=sharing).

A análise dos relatórios de auditoria interna governamental se encontra no [link](https://github.com/BruninSouza/relatorios_auditoria_interna_governamental?tab=readme-ov-file).

## 🗂️ Estrutura do Projeto

```bash
projeto/
├── arquivos-xlsx/              # Pasta onde os arquivos baixados para serem convertidos em colunas
├── codigos/                    # Pasta onde os códigos de automação estão inseridos
├── .gitignore                  # Especifica arquivos que devem ser ignorados pelo sistema de controle de versão
├── DB.xslx                     # BD criado automaticamente com a extração de informação e agrupamento de colunas
├── README.md                   # Este arquivo
└── script.sh                   # Script que executa todas as operações necessárias para criação do BD 
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
chmod +x script.sh
```

Issa dará permissão de execução para o arquivo de script, após isso execute novamente no terminal:

```bash
./script.sh
```
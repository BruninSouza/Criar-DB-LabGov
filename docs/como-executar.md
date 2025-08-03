# **Como Executar o Projeto de Automação de Dados**

Este guia detalha os passos necessários para configurar e executar o projeto completo de automação de dados em seu ambiente local. Siga estas instruções cuidadosamente para garantir uma execução bem-sucedida.

---

## **Pré-requisitos**

Certifique-se de que seu sistema possui as seguintes ferramentas instaladas:

* **Sistema Operacional Linux (preferencialmente Ubuntu 20.04+ ou Debian 11+)**: Este projeto foi desenvolvido e testado em ambientes Linux.
* **Python 3.8+**: Linguagem de programação principal do projeto.
    * Verifique com: `python3 --version`
* **pip**: Gerenciador de pacotes do Python (geralmente vem com o Python).
    * Verifique com: `pip3 --version`
* **Git**: Sistema de controle de versão, essencial para clonar o repositório.
    * Verifique com: `git --version`

---

## **Passos para Execução**

### **1. Clonar o Repositório do Projeto**

Abra seu terminal ou prompt de comando e clone o repositório para sua máquina local através do comando:

```bash
git clone https://github.com/BruninSouza/Criar-DB-LabGov.git
```

Abra-o na IDE de sua escolha e execute o seguinte comando no terminal:

```bash
chmod +x script_main.sh
```

Issa dará permissão de execução para o arquivo de script, após isso execute-o no terminal:

```bash
./script_main.sh
```
#!/bin/bash

echo -e "\nIniciando script de automação...\n"

# Para o script imediatamente se um comando falhar
set -e

# --- 1. Configuração do Ambiente Virtual ---
VENV_DIR="venv"

echo "Verificando o ambiente virtual..."
# Cria o ambiente virtual apenas se a pasta não existir
if [ ! -d "$VENV_DIR" ]; then
    echo "Criando ambiente virtual em '$VENV_DIR'..."
    python3 -m venv $VENV_DIR
else
    echo "Ambiente virtual '$VENV_DIR' já existe."
fi

# Ativa o ambiente virtual
# Nota: Este comando é para shells bash/zsh (Linux/macOS).
# Para Windows, o comando seria: source venv/Scripts/activate
echo -e "\nAtivando o ambiente virtual..."
source $VENV_DIR/bin/activate

# --- 2. Instalação de Dependências ---
REQUIREMENTS_FILE="requirements.txt"

echo -e "\nInstalando dependências de '$REQUIREMENTS_FILE'..."
pip install -r $REQUIREMENTS_FILE

# --- 3. Execução do Script de geração de colunas comuns ---
TARGET_DIR="Ajuste-Colunas-Numericas"

echo -e "\nEntrando no diretório '$TARGET_DIR'..."
cd $TARGET_DIR

echo -e "\nExecutando o Bloco de códigos...\n"
for f in codigos/*.py; do python3 "$f"; done

# --- 4. Retornando ao diretório central ---
echo -e "\nBloco de códigos finalizado. Voltando ao diretório original..."
cd ..

# --- 5. Execução do Script de geração de colunas booleanas ---
TARGET_DIR="Ajuste-Colunas-Booleanas"

echo -e "\nEntrando no diretório '$TARGET_DIR'..."
cd $TARGET_DIR

echo -e "\nExecutando o Bloco de códigos...\n"
for f in codigos/*.py; do python3 "$f"; done

# --- 6. Retornando ao diretório central ---
echo -e "\nBloco de códigos finalizado. Voltando ao diretório original..."
cd ..

# --- 6. Criando banco de dados ---
TARGET_DIR="Atualizar-Dataset"

echo -e "\nEntrando no diretório '$TARGET_DIR'..."
cd $TARGET_DIR

echo -e "\nExecutando o Bloco de códigos...\n"
for f in codigos/*.py; do python3 "$f"; done

# --- 7. Finalização ---
echo -e "\nBloco de códigos finalizado!"

echo -e "\nScript Concluído com sucesso!"
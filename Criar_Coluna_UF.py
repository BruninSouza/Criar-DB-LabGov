import pandas as pd
import re
import unicodedata # Biblioteca para lidar com normalização de texto (acentos)

# --- 1. CONFIGURAÇÃO E CONSTANTES ---
ARQUIVO_ENTRADA = "arquivos-xlsx/DB.xlsx"
ARQUIVO_SAIDA = "DB.xlsx"

# Dicionário que mapeia o NOME COMPLETO (normalizado) para a SIGLA
MAPA_NOME_PARA_SIGLA = {
    'acre': 'AC', 'alagoas': 'AL', 'amapa': 'AP', 'amazonas': 'AM',
    'bahia': 'BA', 'ceara': 'CE', 'distrito federal': 'DF', 'espirito santo': 'ES',
    'goias': 'GO', 'maranhao': 'MA', 'mato grosso': 'MT', 'mato grosso do sul': 'MS',
    'minas gerais': 'MG', 'para': 'PA', 'paraiba': 'PB', 'parana': 'PR',
    'pernambuco': 'PE', 'piaui': 'PI', 'rio de janeiro': 'RJ', 'rio grande do norte': 'RN',
    'rio grande do sul': 'RS', 'rondonia': 'RO', 'roraima': 'RR', 'santa catarina': 'SC',
    'sao paulo': 'SP', 'sergipe': 'SE', 'tocantins': 'TO'
}

# Gera a lista de siglas e o mapa para numérico a partir do dicionário acima
SIGLAS_ESTADOS = list(MAPA_NOME_PARA_SIGLA.values())
MAPA_SIGLA_PARA_NUMERICO = {sigla: i for i, sigla in enumerate(SIGLAS_ESTADOS, 1)}

# --- 2. OTIMIZAÇÃO E FUNÇÕES AUXILIARES ---

# Regex único e compilado para buscar SIGLAS (rápido e prioritário)
PADRAO_SIGLAS_UNICO = re.compile(r'\b(' + '|'.join(SIGLAS_ESTADOS) + r')\b', re.IGNORECASE)

def normalizar_texto(texto):
    """
    Remove acentos, converte para minúsculas e remove caracteres especiais.
    Ex: 'São Paulo!!' -> 'sao paulo'
    """
    # Normaliza para 'NFD' que separa o caractere da sua acentuação
    texto = unicodedata.normalize('NFD', texto)
    # Remove os acentos (caracteres de combinação) e converte para minúsculas
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn').lower()
    return texto

def extrair_localidade_unificado(texto_da_celula):
    """
    Função unificada que extrai a localidade, priorizando a sigla e depois o nome.
    1. Tenta encontrar uma sigla (ex: "SP").
    2. Se não encontrar, normaliza o texto e tenta encontrar um nome de estado (ex: "São Paulo").
    Retorna a sigla correspondente ou None.
    """
    texto_str = str(texto_da_celula)

    # --- ETAPA 1: Busca por SIGLA (mais rápido e específico) ---
    match_sigla = PADRAO_SIGLAS_UNICO.search(texto_str)
    if match_sigla:
        return match_sigla.group(0).upper()

    # --- ETAPA 2: Se não encontrou sigla, busca por NOME COMPLETO ---
    texto_normalizado = normalizar_texto(texto_str)
    
    # Itera sobre os nomes de estado do nosso mapa
    for nome_estado, sigla in MAPA_NOME_PARA_SIGLA.items():
        # Usa \b (fronteira de palavra) para evitar encontrar 'para' em 'preparação'
        if re.search(r'\b' + nome_estado + r'\b', texto_normalizado):
            return sigla # Retorna a sigla correspondente ao nome encontrado

    # Se não encontrou nem sigla nem nome de estado, retorna None
    return None

# --- 3. FUNÇÃO PRINCIPAL PARA ORGANIZAR A LÓGICA ---
def processar_dados_localidade(arquivo_entrada, arquivo_saida):
    """
    Orquestra todo o processo: ler, extrair localidade (sigla ou nome), converter e salvar.
    """
    try:
        df = pd.read_excel(arquivo_entrada)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return

    # Aplica a nova função unificada para criar a coluna de siglas
    df['Sigla_Extraida'] = df['Localidade(s)'].apply(extrair_localidade_unificado)

    # Converte as siglas extraídas para códigos numéricos
    df['UF'] = df['Sigla_Extraida'].map(MAPA_SIGLA_PARA_NUMERICO)

    # Preenche os valores vazios (NaN) na coluna 'UF' com 99 (indefinido)
    df['UF'] = df['UF'].fillna(99).astype(int) # .astype(int) para garantir que sejam inteiros

    # Salva o resultado final (removendo a coluna de sigla intermediária)
    df_final = df.drop(columns=['Sigla_Extraida','Localidade(s)'])
    df_final.to_excel(arquivo_saida, index=False)

    print("\n===Banco de dados Criado com sucesso!!===")
    
# --- 4. PONTO DE ENTRADA DO SCRIPT ---
if __name__ == "__main__":
    processar_dados_localidade(ARQUIVO_ENTRADA, ARQUIVO_SAIDA)
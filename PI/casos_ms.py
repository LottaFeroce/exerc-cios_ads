import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import os
from datetime import datetime

plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("viridis")
arquivo = r"C:\Users\User\Documents\GitHub\exerc-cios_ads\PI\DENGBR25.csv"

ext = os.path.splitext(arquivo)[1].lower()
if ext == ".csv":
    df = pd.read_csv(arquivo, sep=",", encoding="utf-8", low_memory=False)
elif ext in [".xls", ".xlsx"]:
    df = pd.read_excel(arquivo)
else:
    raise ValueError("Formato de arquivo não suportado. Use .csv ou .xlsx")

df.columns = df.columns.str.strip().str.upper()

mapa_uf = {
    12: "AC", 27: "AL", 13: "AM", 16: "AP", 29: "BA", 23: "CE",
    53: "DF", 32: "ES", 52: "GO", 21: "MA", 31: "MG", 50: "MS",
    51: "MT", 15: "PA", 25: "PB", 26: "PE", 22: "PI", 41: "PR",
    33: "RJ", 24: "RN", 43: "RS", 11: "RO", 14: "RR", 42: "SC",
    28: "SE", 35: "SP", 17: "TO"
}

# CORREÇÃO: Mapa de municípios com códigos de 6 dígitos (conforme seu dataset)
mapa_municipios_ms = {
    # Códigos de 6 dígitos conforme mostrado no seu output
    500800: "Terenos",
    500630: "Paranaíba", 
    500270: "Campo Grande",  # Capital
    500470: "Ivinhema",
    500020: "Água Clara",
    500440: "Inocência",
    500295: "Chapadão do Sul",
    500830: "Três Lagoas",
    500540: "Maracaju",
    500320: "Corumbá",
    500370: "Dourados",
    500620: "Nova Andradina",
    500790: "Sidrolândia",
    500110: "Aquidauana",
    500660: "Ponta Porã",
    500560: "Miranda",
    500570: "Naviraí",
    500240: "Caarapó",
    500600: "Nova Alvorada do Sul",
    500580: "Nioaque",
    500710: "Ribas do Rio Pardo",
    500720: "Rio Brilhante",
    500500: "Jardim",
    500310: "Corguinho",
    500840: "Vicentina",
    500750: "Rochedo",
    500390: "Figueirão",
    500525: "Laguna Carapã",
    500150: "Bandeirantes",
    500210: "Bela Vista",
    500220: "Bonito",
    500230: "Brasilândia",
    500260: "Camapuã",
    500280: "Caracol",
    500290: "Cassilândia",
    500330: "Coxim",
    500345: "Deodápolis",
    500348: "Dois Irmãos do Buriti",
    500350: "Douradina",
    500375: "Eldorado",
    500380: "Fátima do Sul",
    500400: "Glória de Dourados",
    500410: "Guia Lopes da Laguna",
    500430: "Iguatemi",
    500450: "Itaporã",
    500460: "Itaquiraí",
    500480: "Japorã",
    500490: "Jaraguari",
    500510: "Jateí",
    500515: "Juti",
    500520: "Ladário",
    500568: "Mundo Novo",
    500625: "Novo Horizonte do Sul",
    500627: "Paraíso das Águas",
    500635: "Paranhos",
    500640: "Pedro Gomes",
    500690: "Porto Murtinho",
    500730: "Rio Negro",
    500740: "Rio Verde de Mato Grosso",
    500755: "Santa Rita do Pardo",
    500769: "São Gabriel do Oeste",
    500770: "Sete Quedas",
    500780: "Selvíria",
    500793: "Sonora",
    500795: "Tacuru",
    500797: "Taquarussu"
}

if "SG_UF" in df.columns:
    if pd.api.types.is_numeric_dtype(df["SG_UF"]):
        df["UF"] = df["SG_UF"].map(mapa_uf)
    else:
        df["UF"] = df["SG_UF"].str.upper().str.strip()
else:
    df["UF"] = None

for col in ["DT_NOTIFIC", "DT_SIN_PRI"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# CORREÇÃO: Verificar o ano real dos dados - escolher o ano com MAIS dados
def analisar_datas(df):
    """Analisa as datas reais do dataset e escolhe o ano com mais dados"""
    if "DT_NOTIFIC" not in df.columns:
        print("Coluna DT_NOTIFIC não encontrada")
        return df, "Desconhecido"
    
    # Verificar distribuição por ano
    df_temp = df.dropna(subset=["DT_NOTIFIC"]).copy()
    df_temp["ANO"] = df_temp["DT_NOTIFIC"].dt.year
    distribuicao_ano = df_temp["ANO"].value_counts().sort_values(ascending=False)  # Ordenar por quantidade
    
    print("=== ANÁLISE DE DATAS DO DATASET ===")
    print("Distribuição por ano (ordenado por quantidade):")
    for ano, count in distribuicao_ano.items():
        print(f"  {ano}: {count:,} casos ({count/len(df_temp)*100:.1f}%)")
    
    # CORREÇÃO: Determinar ano principal (ano com MAIOR quantidade de dados)
    ano_principal = distribuicao_ano.index[0] if len(distribuicao_ano) > 0 else "Desconhecido"
    print(f"Ano principal dos dados: {ano_principal} (com {distribuicao_ano[ano_principal]:,} casos)")
    print(f"Período total: {df_temp['DT_NOTIFIC'].min().strftime('%d/%m/%Y')} a {df_temp['DT_NOTIFIC'].max().strftime('%d/%m/%Y')}")
    
    return df, ano_principal

# Analisar datas primeiro
df, ano_principal = analisar_datas(df)

# CORREÇÃO: Filtrar apenas datas futuras específicas
def filtrar_datas_futuras(df):
    """Remove apenas datas futuras específicas"""
    data_atual = datetime.now()
    
    # Contar registros antes do filtro
    total_antes = len(df)
    
    # Remover apenas datas que são futuras em relação à data atual
    if "DT_NOTIFIC" in df.columns:
        mask_futuras = df["DT_NOTIFIC"] <= data_atual
        df_filtrado = df[mask_futuras].copy()
        
        # Contar registros após o filtro
        total_depois = len(df_filtrado)
        
        removidos = total_antes - total_depois
        print(f"Removidas {removidos} registros com datas futuras")
        
        if removidos > 0:
            print(f"Período após filtro: {df_filtrado['DT_NOTIFIC'].min().strftime('%d/%m/%Y')} a {df_filtrado['DT_NOTIFIC'].max().strftime('%d/%m/%Y')}")
        
        return df_filtrado
    else:
        return df

# Aplicar filtro de datas (apenas remove futuras)
df = filtrar_datas_futuras(df)

if "DT_NOTIFIC" in df.columns:
    df["MES_NOTIFIC"] = df["DT_NOTIFIC"].dt.month
    df["ANO_NOTIFIC"] = df["DT_NOTIFIC"].dt.year

df = df.dropna(subset=["DT_NOTIFIC", "UF"])
df = df[df["UF"].isin(mapa_uf.values())]

print(f"\n=== DADOS FINAIS ===")
print(f"Registros válidos: {len(df):,}")
print(f"Estados distintos: {df['UF'].nunique()}")
if "DT_NOTIFIC" in df.columns:
    print(f"Período final: {df['DT_NOTIFIC'].min().strftime('%d/%m/%Y')} a {df['DT_NOTIFIC'].max().strftime('%d/%m/%Y')}")

# CORREÇÃO: Usar o ano real detectado automaticamente (agora com a lógica correta)
def obter_ano_dataset():
    """Retorna o ano principal do dataset - o ano com mais dados"""
    return ano_principal

# CORREÇÃO: Função melhorada para estatísticas de MS
def estatisticas_ms():
    df_ms = df[df["UF"] == "MS"]
    
    print(f"\n=== ESTATÍSTICAS MATO GROSSO DO SUL ===")
    print(f"Total de casos em MS: {len(df_ms):,}")
    if len(df_ms) > 0:
        print(f"Período: {df_ms['DT_NOTIFIC'].min().strftime('%d/%m/%Y')} a {df_ms['DT_NOTIFIC'].max().strftime('%d/%m/%Y')}")
        print(f"Proporção nacional: {(len(df_ms)/len(df)*100):.2f}%")
        
        # Verificar dados de idade
        if "NU_IDADE_N" in df_ms.columns:
            idade_valida = df_ms["NU_IDADE_N"].notna() & df_ms["NU_IDADE_N"].between(0, 120)
            print(f"Dados de idade válidos: {idade_valida.sum():,} ({idade_valida.sum()/len(df_ms)*100:.1f}%)")
    return df_ms

# Função para filtrar dados de MS
def filtrar_ms():
    return df[df["UF"] == "MS"]

# CORREÇÃO: Atualizar função grafico_mensal para usar ano real
def grafico_mensal():
    # Pegar apenas os meses que existem nos dados
    casos_mes = df["MES_NOTIFIC"].value_counts().sort_index()
    
    # Criar labels dos meses
    meses_nomes = {
        1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
        7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
    }
    
    # Aplicar nomes aos meses
    casos_mes_index = [meses_nomes.get(mes, f"Mês {mes}") for mes in casos_mes.index]
    
    # Usar o ano real detectado (agora 2025)
    ano_real = obter_ano_dataset()
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(casos_mes_index, casos_mes.values, color="royalblue", alpha=0.8)
    plt.title(f"Casos de Dengue por Mês ({ano_real})")
    plt.xlabel("Mês")
    plt.ylabel("Número de Casos")
    
    # Adicionar valores nas barras
    for bar, valor in zip(bars, casos_mes.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (valor * 0.01),
                f"{valor:,}", ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()

# CORREÇÃO: Atualizar função de evolução mensal para usar ano real
def grafico_top5_estados_mensal():
    casos_uf = df["UF"].value_counts().sort_values(ascending=False)
    top5 = casos_uf.head(5).index
    
    # Agrupar por UF e mês
    casos_mensais = df.groupby(["UF", "MES_NOTIFIC"]).size().reset_index(name="CASOS")
    pivot = casos_mensais.pivot(index="MES_NOTIFIC", columns="UF", values="CASOS")
    
    # Manter apenas os top 5 e preencher meses faltantes com 0
    pivot = pivot[top5].fillna(0)
    
    # Criar labels dos meses
    meses_nomes = {
        1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
        7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
    }
    pivot.index = [meses_nomes.get(mes, f"Mês {mes}") for mes in pivot.index]
    
    # Usar o ano real detectado (agora 2025)
    ano_real = obter_ano_dataset()
    
    plt.figure(figsize=(12, 6))
    pivot.plot(ax=plt.gca(), marker="o", linewidth=2.5)
    plt.title(f"Evolução Mensal dos Casos (Top 5 Estados) - {ano_real}")
    plt.xlabel("Mês")
    plt.ylabel("Número de Casos")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(title="UF")
    plt.tight_layout()
    plt.show()

# CORREÇÃO: Atualizar todas as funções para usar ano real
def grafico_top10_estados():
    casos_uf = df["UF"].value_counts().sort_values(ascending=False)
    top10 = casos_uf.head(10)
    
    # Usar o ano real detectado (agora 2025)
    ano_real = obter_ano_dataset()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top10.index, y=top10.values)
    plt.title(f"Top 10 Estados com Mais Casos de Dengue ({ano_real})")
    plt.xlabel("Estado (UF)")
    plt.ylabel("Número de Casos")
    for i, v in enumerate(top10.values):
        plt.text(i, v + (v * 0.01), f"{v:,}", ha="center", fontsize=8)
    plt.tight_layout()
    plt.show()

def grafico_sexo():
    if "CS_SEXO" in df.columns:
        casos_sexo = df["CS_SEXO"].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(
            casos_sexo, labels=casos_sexo.index,
            autopct="%1.1f%%", startangle=90,
            colors=["#6495ED", "#FF69B4", "#D3D3D3"]
        )
        plt.title("Distribuição de Casos por Sexo Biológico")
        plt.tight_layout()
        plt.show()

def grafico_faixa_etaria():
    if "NU_IDADE_N" in df.columns:
        df_valid = df[df["NU_IDADE_N"].between(0, 120)].copy()
        bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 120]
        labels = ["0–9", "10–19", "20–29", "30–39", "40–49", "50–59", "60–69", "70–79", "80+"]
        df_valid["FAIXA_ETARIA"] = pd.cut(df_valid["NU_IDADE_N"], bins=bins, labels=labels, right=False)
        faixa = df_valid["FAIXA_ETARIA"].value_counts().sort_index()
        plt.figure(figsize=(12, 6))
        sns.barplot(x=faixa.index, y=faixa.values, color="#FF8C00")
        plt.title("Distribuição de Casos por Faixa Etária")
        plt.xlabel("Faixa Etária (anos)")
        plt.ylabel("Número de Casos")
        plt.tight_layout()
        plt.show()

def grafico_mapa_brasil():
    print(" Gerando mapa de calor do Brasil...")
    try:
        estados = gpd.read_file("https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson")
        casos_uf = df["UF"].value_counts().reset_index()
        casos_uf.columns = ["sigla", "casos"]
        mapa = estados.merge(casos_uf, left_on="sigla", right_on="sigla", how="left")
        
        # Usar o ano real detectado (agora 2025)
        ano_real = obter_ano_dataset()
        
        plt.figure(figsize=(10, 8))
        mapa.plot(column="casos", cmap="Reds", legend=True, edgecolor="black")
        plt.title(f"Mapa de Calor – Casos de Dengue por Estado ({ano_real})")
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f" Erro ao gerar mapa: {e}")

# CORREÇÃO: Atualizar análise MS para usar ano real
def analise_ms():
    df_ms = filtrar_ms()
    
    if df_ms.empty:
        print("Não há dados disponíveis para o Mato Grosso do Sul.")
        return
    
    estatisticas_ms()
    
    # Casos por mês em MS - com correção
    casos_mes_ms = df_ms["MES_NOTIFIC"].value_counts().sort_index()
    
    # Aplicar nomes aos meses
    meses_nomes = {
        1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
        7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
    }
    casos_mes_ms_index = [meses_nomes.get(mes, f"Mês {mes}") for mes in casos_mes_ms.index]
    
    # Usar o ano real detectado (agora 2025)
    ano_real = obter_ano_dataset()
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(casos_mes_ms_index, casos_mes_ms.values, color="green", alpha=0.8)
    plt.title(f"Casos de Dengue no Mato Grosso do Sul por Mês ({ano_real})")
    plt.xlabel("Mês")
    plt.ylabel("Número de Casos")
    
    for bar, valor in zip(bars, casos_mes_ms.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (valor * 0.01),
                f"{valor:,}", ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()
    
    # Distribuição por sexo em MS
    if "CS_SEXO" in df_ms.columns:
        casos_sexo_ms = df_ms["CS_SEXO"].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(
            casos_sexo_ms, labels=casos_sexo_ms.index,
            autopct="%1.1f%%", startangle=90,
            colors=["#2E8B57", "#98FB98", "#D3D3D3"]
        )
        plt.title("Distribuição de Casos por Sexo - MS")
        plt.tight_layout()
        plt.show()

# Resto das funções permanecem iguais...
def grafico_faixa_etaria_ms():
    df_ms = filtrar_ms()
    
    if df_ms.empty:
        print("Não há dados disponíveis para o Mato Grosso do Sul.")
        return
    
    if "NU_IDADE_N" in df_ms.columns:
        df_ms_idade = df_ms.dropna(subset=["NU_IDADE_N"]).copy()
        
        if not pd.api.types.is_numeric_dtype(df_ms_idade["NU_IDADE_N"]):
            df_ms_idade["NU_IDADE_N"] = pd.to_numeric(df_ms_idade["NU_IDADE_N"], errors='coerce')
        
        df_ms_valid = df_ms_idade[df_ms_idade["NU_IDADE_N"].between(0, 120)]
        
        if df_ms_valid.empty:
            print("Não há dados de idade válidos para MS.")
            return
            
        print(f"Casos com idade válida em MS: {len(df_ms_valid):,}")
        
        bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 120]
        labels = ["0–9", "10–19", "20–29", "30–39", "40–49", "50–59", "60–69", "70–79", "80+"]
        
        df_ms_valid["FAIXA_ETARIA"] = pd.cut(df_ms_valid["NU_IDADE_N"], bins=bins, labels=labels, right=False)
        faixa_ms = df_ms_valid["FAIXA_ETARIA"].value_counts().sort_index()
        
        plt.figure(figsize=(12, 6))
        bars = plt.bar(faixa_ms.index, faixa_ms.values, color="#32CD32")
        plt.title("Distribuição de Casos por Faixa Etária - Mato Grosso do Sul")
        plt.xlabel("Faixa Etária (anos)")
        plt.ylabel("Número de Casos")
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height):,}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
    else:
        print("Coluna 'NU_IDADE_N' não encontrada.")

def ranking_municipios_ms():
    df_ms = filtrar_ms()
    
    if df_ms.empty:
        print("Não há dados disponíveis para o Mato Grosso do Sul.")
        return
    
    print(f"\nTotal de casos em MS para análise: {len(df_ms):,}")
    
    # Encontrar a coluna correta de município
    municipio_col = None
    for col in ["ID_MUNICIP", "ID_MN_RESI", "MUNICIPIO", "ID_MUNICIP"]:
        if col in df_ms.columns:
            municipio_col = col
            print(f"Usando coluna: {municipio_col}")
            break
    
    if municipio_col:
        # CORREÇÃO: Converter códigos para nomes de municípios (6 dígitos)
        df_ms_copy = df_ms.copy()
        
        # Verificar se a coluna tem códigos numéricos
        if pd.api.types.is_numeric_dtype(df_ms_copy[municipio_col]):
            print("Convertendo códigos numéricos (6 dígitos) para nomes de municípios...")
            df_ms_copy["MUNICIPIO_NOME"] = df_ms_copy[municipio_col].map(mapa_municipios_ms)
            
            # Para códigos não mapeados, manter o código formatado
            missing_mask = df_ms_copy["MUNICIPIO_NOME"].isna()
            df_ms_copy.loc[missing_mask, "MUNICIPIO_NOME"] = df_ms_copy.loc[missing_mask, municipio_col].apply(
                lambda x: f"Município {x}" if pd.notna(x) else "Não informado"
            )
            
            coluna_para_uso = "MUNICIPIO_NOME"
        else:
            coluna_para_uso = municipio_col
        
        # Contar casos
        casos_municipio = df_ms_copy[coluna_para_uso].value_counts()
        
        print(f"\nEstatísticas dos municípios:")
        print(f"Total de municípios com casos: {len(casos_municipio)}")
        print(f"Maior número de casos: {casos_municipio.max():,}")
        print(f"Menor número de casos: {casos_municipio.min():,}")
        
        # Pegar top 10
        top_municipios = casos_municipio.head(10)
        
        print(f"\nTop 10 municípios:")
        for i, (municipio, casos) in enumerate(top_municipios.items(), 1):
            print(f"{i:2d}. {municipio}: {casos:,} casos")
        
        # Plotar gráfico
        plt.figure(figsize=(14, 8))
        
        # CORREÇÃO: Gráfico horizontal com nomes legíveis
        bars = plt.barh(range(len(top_municipios)), top_municipios.values, color="lightgreen", edgecolor="darkgreen")
        
        # Configurar labels dos municípios
        plt.yticks(range(len(top_municipios)), top_municipios.index, fontsize=10)
        plt.title("Top 10 Municípios com Mais Casos - Mato Grosso do Sul", fontsize=14, fontweight='bold')
        plt.xlabel("Número de Casos", fontsize=12)
        plt.ylabel("Município", fontsize=12)
        
        # Adicionar valores nas barras
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width + (width * 0.01), bar.get_y() + bar.get_height()/2.,
                    f'{int(width):,}', va='center', fontsize=10, fontweight='bold')
        
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.show()
        
    else:
        print("Nenhuma coluna de município encontrada no dataset.")

def menu():
    opcoes = {
        "1": ("Top 10 Estados", grafico_top10_estados),
        "2": ("Casos por Mês", grafico_mensal),
        "3": ("Evolução Mensal (Top 5 UF)", grafico_top5_estados_mensal),
        "4": ("Casos por Sexo", grafico_sexo),
        "5": ("Casos por Faixa Etária", grafico_faixa_etaria),
        "6": ("Mapa de Calor do Brasil", grafico_mapa_brasil),
        "7": ("Análise Completa - MS", analise_ms),
        "8": ("Top Municípios - MS", ranking_municipios_ms),
        "9": ("Faixa Etária - MS", grafico_faixa_etaria_ms),
        "0": ("Sair", None)
    }

    while True:
        print("\n === MENU DE ANÁLISES ===")
        for k, (desc, _) in opcoes.items():
            print(f"[{k}] {desc}")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Saindo da visualização.")
            break
        elif escolha in opcoes:
            print(f"\n Exibindo: {opcoes[escolha][0]}")
            plt.close('all')
            opcoes[escolha][1]()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    estatisticas_ms()
    menu()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# === CONFIGURAÇÕES ===
plt.style.use("seaborn-v0_8-whitegrid")

# Caminho do dataset
arquivo = r"C:\Users\User\Documents\GitHub\exerc-cios_ads\PI\DENGBR25.csv"
df = pd.read_csv(arquivo, sep=",", encoding="utf-8", low_memory=False)

# === PADRONIZAÇÃO DAS COLUNAS ===
df.columns = df.columns.str.strip().str.upper()

# === MAPA DE CÓDIGOS IBGE → UF ===
mapa_uf = {
    12: "AC", 27: "AL", 13: "AM", 16: "AP", 29: "BA", 23: "CE",
    53: "DF", 32: "ES", 52: "GO", 21: "MA", 31: "MG", 50: "MS",
    51: "MT", 15: "PA", 25: "PB", 26: "PE", 22: "PI", 41: "PR",
    33: "RJ", 24: "RN", 43: "RS", 11: "RO", 14: "RR", 42: "SC",
    28: "SE", 35: "SP", 17: "TO"
}
if "SG_UF" in df.columns:
    df["SG_UF"] = df["SG_UF"].replace(mapa_uf)

# === CONVERSÃO DE DATAS ===
for col in ["DT_NOTIFIC", "DT_SIN_PRI"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

df = df.dropna(subset=["DT_NOTIFIC"])
df["MES_NOTIFIC"] = df["DT_NOTIFIC"].dt.month
df["ANO_NOTIFIC"] = df["DT_NOTIFIC"].dt.year

# === FAIXA ETÁRIA ===
if "NU_IDADE_N" in df.columns:
    df = df[df["NU_IDADE_N"].between(0, 120)]
    bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 120]
    labels = ["0–9", "10–19", "20–29", "30–39", "40–49", "50–59", "60–69", "70–79", "80+"]
    df["FAIXA_ETARIA"] = pd.cut(df["NU_IDADE_N"], bins=bins, labels=labels, right=False)

# === FUNÇÕES DE VISUALIZAÇÃO ===

def grafico_top10_estados():
    casos_uf = df["SG_UF"].value_counts().sort_values(ascending=False)
    top10 = casos_uf.head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top10.index, y=top10.values, palette="viridis")
    plt.title("Top 10 Estados com Mais Casos de Dengue (2025)")
    plt.xlabel("Estado (UF)")
    plt.ylabel("Número de Casos")
    plt.tight_layout()
    plt.show()

def grafico_mensal():
    casos_mes = df["MES_NOTIFIC"].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=casos_mes.index, y=casos_mes.values, color="royalblue")
    plt.title("Casos de Dengue por Mês (2025)")
    plt.xlabel("Mês")
    plt.ylabel("Número de Casos")
    plt.tight_layout()
    plt.show()

def grafico_top5_estados_mensal():
    casos_uf = df["SG_UF"].value_counts().sort_values(ascending=False)
    top5_ufs = casos_uf.head(5).index
    casos_mensais = df.groupby(["SG_UF", "MES_NOTIFIC"]).size().reset_index(name="CASOS")
    pivot = casos_mensais.pivot(index="MES_NOTIFIC", columns="SG_UF", values="CASOS")
    plt.figure(figsize=(12, 6))
    pivot[top5_ufs].plot(ax=plt.gca(), marker="o")
    plt.title("Evolução Mensal dos Casos (Top 5 Estados)")
    plt.xlabel("Mês")
    plt.ylabel("Número de Casos")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(title="UF")
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
    faixa = df["FAIXA_ETARIA"].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=faixa.index, y=faixa.values, color="#FF8C00")
    plt.title("Distribuição de Casos por Faixa Etária")
    plt.xlabel("Faixa Etária (anos)")
    plt.ylabel("Número de Casos")
    plt.tight_layout()
    plt.show()

def grafico_mapa_brasil():
    print("⏳ Gerando mapa de calor do Brasil...")
    try:
        estados = gpd.read_file("https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson")
        casos_uf = df["SG_UF"].value_counts().reset_index()
        casos_uf.columns = ["sigla", "casos"]

        mapa = estados.merge(casos_uf, left_on="sigla", right_on="sigla", how="left")
        plt.figure(figsize=(10, 8))
        mapa.plot(column="casos", cmap="Reds", legend=True, edgecolor="black")
        plt.title("Mapa de Calor – Casos de Dengue por Estado (2025)")
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"⚠️ Erro ao gerar mapa: {e}")

def grafico_media_idade_por_uf():
    if "NU_IDADE_N" in df.columns:
        media = df.groupby("SG_UF")["NU_IDADE_N"].mean().sort_values(ascending=False)
        plt.figure(figsize=(12, 6))
        sns.barplot(x=media.index, y=media.values, palette="crest")
        plt.title("Média de Idade dos Casos por Estado")
        plt.xlabel("UF")
        plt.ylabel("Idade Média")
        plt.tight_layout()
        plt.show()

# === MENU INTERATIVO ===
def menu():
    opcoes = {
        "1": ("Top 10 Estados", grafico_top10_estados),
        "2": ("Casos por Mês", grafico_mensal),
        "3": ("Evolução Mensal (Top 5 UF)", grafico_top5_estados_mensal),
        "4": ("Casos por Sexo", grafico_sexo),
        "5": ("Casos por Faixa Etária", grafico_faixa_etaria),
        "6": ("Média de Idade por Estado", grafico_media_idade_por_uf),
        "7": ("Mapa de Calor do Brasil", grafico_mapa_brasil),
        "0": ("Sair", None)
    }

    while True:
        print("\n📊 === MENU DE ANÁLISES ===")
        for k, (desc, _) in opcoes.items():
            print(f"[{k}] {desc}")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Saindo da visualização.")
            break
        elif escolha in opcoes:
            print(f"\n🔹 Exibindo: {opcoes[escolha][0]}")
            plt.close('all')
            opcoes[escolha][1]()
        else:
            print("Opção inválida, tente novamente.")

# === EXECUÇÃO ===
if __name__ == "__main__":
    menu()

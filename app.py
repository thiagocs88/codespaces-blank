import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Título
# -----------------------------
st.title("☕ Café & Cia")
st.write("Dashboard de vendas da cafeteria")

# -----------------------------
# Carregamento dos dados
# -----------------------------
df = pd.read_csv("vendas_cafeteria.csv")
df["data"] = pd.to_datetime(
    df["data"],
    format="%d/%m/%Y"
)

# -----------------------------
# Indicadores (Dados na Íntegra)
# -----------------------------
faturamento = df["valor"].sum()
quantidade = df["quantidade"].sum()

col1, col2 = st.columns(2)
col1.metric(
    "Faturamento Total",
    f"R$ {faturamento:,.2f}"
)
col2.metric(
    "Total de Itens vendidos",
    quantidade
)

# -----------------------------
# Vendas por produto
# -----------------------------
vendas_produto = (
    df
    .groupby("produto")["valor"]
    .sum()
    .reset_index()
)

# -----------------------------
# Gráfico
# -----------------------------
fig = px.bar(
    vendas_produto,
    x="produto",
    y="valor",
    title="Vendas por Produto (Geral)",
    text_auto=",.2f"  # Adiciona o valor em cima de cada barra automaticamente
)
st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Dados
# -----------------------------
st.subheader("Dados utilizados")
st.dataframe(
    df,
    use_container_width=True
)

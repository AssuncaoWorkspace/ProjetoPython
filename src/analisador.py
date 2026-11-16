from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class AnalisadorDeDados:
    """Classe responsável pela leitura, limpeza e análise do dataset."""

    def __init__(self, caminho_csv: str | Path):
        self.caminho_csv = Path(caminho_csv)
        self.df = self._carregar_dados()

    def _carregar_dados(self) -> pd.DataFrame:
        if not self.caminho_csv.exists():
            raise FileNotFoundError(f"Arquivo de dados não encontrado: {self.caminho_csv}")

        df = pd.read_csv(self.caminho_csv)

        df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

        colunas_esperadas = ["mes", "produto", "categoria", "segmento", "quantidade", "valor_venda"]
        for coluna in colunas_esperadas:
            if coluna not in df.columns:
                raise ValueError(f"A coluna '{coluna}' precisa existir no dataset para análise.")

        df["mes"] = pd.to_datetime(df["mes"], errors="coerce")
        df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
        df["valor_venda"] = pd.to_numeric(df["valor_venda"], errors="coerce")

        df["produto"] = df["produto"].fillna("Produto não informado")
        df["categoria"] = df["categoria"].fillna("Sem categoria")
        df["segmento"] = df["segmento"].fillna("Sem segmento")

        df = df.dropna(subset=["mes", "produto", "categoria", "segmento", "quantidade", "valor_venda"]).reset_index(drop=True)

        if df.empty:
            raise ValueError("O dataset ficou vazio após a limpeza inicial.")

        return df

    def resumo_dados(self) -> str:
        total_vendas = self.df["valor_venda"].sum()
        total_itens = self.df["quantidade"].sum()
        periodo = self.df["mes"].min().strftime("%b/%Y") + " a " + self.df["mes"].max().strftime("%b/%Y")
        produtos = self.df["produto"].nunique()

        return (
            f"Período analisado: {periodo}\n"
            f"Total de vendas: R$ {total_vendas:,.2f}\n"
            f"Quantidade de itens vendidos: {total_itens:,.0f}\n"
            f"Produtos monitorados: {produtos}"
        )

    def gerar_grafico_linha(self, caminho_saida: str | Path = "outputs/grafico_linha.png") -> str:
        dados = (
            self.df.groupby("mes", as_index=False)["valor_venda"]
            .sum()
            .sort_values("mes")
        )

        plt.figure(figsize=(10, 6))
        plt.plot(dados["mes"], dados["valor_venda"], marker="o", linewidth=2, color="#1f77b4")
        plt.title("Evolução das Vendas por Mês")
        plt.xlabel("Mês")
        plt.ylabel("Valor em R$")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()

        destino = Path(caminho_saida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(destino, dpi=200)
        plt.close()
        return str(destino)

    def gerar_grafico_barras(self, caminho_saida: str | Path = "outputs/grafico_barras.png") -> str:
        top_produtos = (
            self.df.groupby("produto", as_index=False)["valor_venda"]
            .sum()
            .sort_values("valor_venda", ascending=False)
            .head(5)
        )

        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=top_produtos,
            x="produto",
            y="valor_venda",
            hue="produto",
            palette="viridis",
            dodge=False,
            legend=False,
        )
        plt.title("Top 5 Produtos por Receita")
        plt.xlabel("Produto")
        plt.ylabel("Receita em R$")
        plt.xticks(rotation=20)
        plt.tight_layout()

        destino = Path(caminho_saida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(destino, dpi=200)
        plt.close()
        return str(destino)

    def gerar_histograma(self, caminho_saida: str | Path = "outputs/histograma_quantidade.png") -> str:
        dados = self.df[self.df["quantidade"] > 0]

        plt.figure(figsize=(10, 6))
        plt.hist(dados["quantidade"], bins=12, edgecolor="black", color="#4CAF50")
        plt.title("Distribuição da Quantidade Vendida")
        plt.xlabel("Quantidade")
        plt.ylabel("Frequência")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()

        destino = Path(caminho_saida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(destino, dpi=200)
        plt.close()
        return str(destino)

    def mostrar_dados(self, linhas: int = 5) -> pd.DataFrame:
        return self.df.head(linhas)

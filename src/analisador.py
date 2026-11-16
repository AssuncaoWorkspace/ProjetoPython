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

        dados_originais = pd.read_csv(self.caminho_csv)
        dados_originais.columns = [
            str(coluna).strip().lower().replace(" ", "_")
            for coluna in dados_originais.columns
        ]
        dados_originais = dados_originais.rename(
            columns={
                "sepallengthcm": "sepal_lengthcm",
                "sepalwidthcm": "sepal_widthcm",
                "petallengthcm": "petal_lengthcm",
                "petalwidthcm": "petal_widthcm",
            }
        )

        colunas_esperadas = [
            "sepal_lengthcm",
            "sepal_widthcm",
            "petal_lengthcm",
            "petal_widthcm",
            "species",
        ]
        for coluna in colunas_esperadas:
            if coluna not in dados_originais.columns:
                raise ValueError(f"A coluna '{coluna}' precisa existir no dataset para análise.")

        medidas = [
            "sepal_lengthcm",
            "sepal_widthcm",
            "petal_lengthcm",
            "petal_widthcm",
        ]
        for coluna in medidas:
            dados_originais[coluna] = pd.to_numeric(
                dados_originais[coluna],
                errors="coerce",
            )

        df = dados_originais[medidas + ["species"]].dropna().reset_index(drop=True)

        if df.empty:
            raise ValueError("O dataset ficou vazio após a limpeza inicial.")

        return df

    def resumo_dados(self) -> str:
        especies = sorted(self.df["species"].unique())
        media_petala = self.df["petal_lengthcm"].mean()

        return (
            f"Amostras analisadas: {len(self.df):,}\n"
            f"Espécies identificadas: {len(especies)} ({', '.join(especies)})\n"
            f"Comprimento médio da pétala: {media_petala:.2f} cm"
        )

    def gerar_grafico_barras(self, caminho_saida: str | Path = "outputs/media_petala_por_especie.png") -> str:
        dados = (
            self.df.groupby("species", as_index=False)["petal_lengthcm"]
            .mean()
            .sort_values("petal_lengthcm", ascending=False)
        )

        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=dados,
            x="species",
            y="petal_lengthcm",
            hue="species",
            palette="viridis",
            legend=False,
        )
        plt.title("Comprimento Médio da Pétala por Espécie")
        plt.xlabel("Espécie")
        plt.ylabel("Comprimento médio da pétala (cm)")
        plt.tight_layout()

        destino = Path(caminho_saida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(destino, dpi=200)
        plt.close()
        return str(destino)

    def gerar_grafico_dispersao(self, caminho_saida: str | Path = "outputs/dispersao_iris.png") -> str:
        dados = self.df[
            (self.df["sepal_lengthcm"] > 0) & (self.df["sepal_widthcm"] > 0)
        ]

        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=dados,
            x="sepal_lengthcm",
            y="sepal_widthcm",
            hue="species",
            palette="viridis",
            s=65,
        )
        plt.title("Relação entre Comprimento e Largura das Sépalas")
        plt.xlabel("Comprimento da sépala (cm)")
        plt.ylabel("Largura da sépala (cm)")
        plt.legend(title="Espécie")
        plt.grid(True, linestyle="--", alpha=0.4)
        plt.tight_layout()

        destino = Path(caminho_saida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(destino, dpi=200)
        plt.close()
        return str(destino)

    def gerar_histograma(self, caminho_saida: str | Path = "outputs/distribuicao_petalas.png") -> str:
        dados = self.df[self.df["petal_lengthcm"] > 0]

        plt.figure(figsize=(10, 6))
        sns.histplot(
            data=dados,
            x="petal_lengthcm",
            hue="species",
            bins=15,
            multiple="layer",
            alpha=0.55,
            palette="viridis",
        )
        plt.title("Distribuição do Comprimento das Pétalas")
        plt.xlabel("Comprimento da pétala (cm)")
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

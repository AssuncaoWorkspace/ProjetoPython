
# Projeto: Análise de Dados com Python

**Disciplina:** Linguagem de Programação em Python (2026.2)  
**Professor:** Ruben Prado  
**Instituição:** Faculdade Senac-DF de Tecnologia e Inovação

---

## Objetivo do Projeto
Este projeto analisa medidas de flores Iris em um Sistema Analítico Interativo (CLI), aplicando Pandas, orientação a objetos, Matplotlib e Seaborn para comparar as três espécies da base.

---

## Estrutura do Repositório

```text
projeto-integrador-python/
│
├── data/
│   ├── iris.csv       # train.csv do Kaggle Superstore Sales Dataset
│   └── .gitkeep
│
├── src/
│   ├── __init__.py
│   └── analisador.py
│
├── outputs/
│   └── (gráficos gerados pela execução)
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Requisitos Técnicos Obrigatórios

1. Menu interativo em `main.py` com loop contínuo e tratamento de valor inválido com `try/except ValueError`.
2. Classe `AnalisadorDeDados` em `src/analisador.py` com leitura do CSV via Pandas e limpeza com `dropna()`.
3. Geração de três tipos de gráfico (barras, dispersão e histograma), usando agrupamento ou filtros booleanos antes da plotagem.
4. Cada gráfico possui título e nomes nos eixos.

---

## Instalação e Execução Local

```bash
pip install -r requirements.txt
python main.py
```

---

## 📝 Formulário Oficial de Entrega

### 👥 Integrantes da Equipe

* Gabriel Assunção - 62027256
* Diego Serra - 62501576
* Pedro Maia - 62056976

### 🗂️ Sobre o Dataset Escolhido

* **Tema Geral:** Medidas de flores e classificação de espécies de Iris
* **Fonte de Dados (URL):** [Iris Species no Kaggle](https://www.kaggle.com/datasets/uciml/iris)
* **Arquivo utilizado:** `Iris.csv`, armazenado no projeto como `data/iris.csv`. A base possui 150 amostras e seis colunas; o Kaggle identifica a licença como CC0 (domínio público).
* **Motivação:** A base reúne medidas de sépalas e pétalas de três espécies de Iris. A análise compara essas medidas para observar como os atributos florais variam entre as espécies.

### 🏗️ Arquitetura e Estruturação

* **Módulos / Classes Criadas:** A classe `AnalisadorDeDados` em `src/analisador.py` centraliza a leitura do CSV, a conversão das medidas numéricas, a limpeza e a geração dos gráficos.
* **Limpeza de Dados:** As quatro medidas são convertidas para números e `dropna()` remove amostras com medidas ou espécie ausentes. O arquivo original contém 150 amostras das três espécies.

### 📊 Gráficos Desenvolvidos

1. **Visão 1:** Gráfico de barras comparando o comprimento médio das pétalas entre as espécies.
2. **Visão 2:** Gráfico de dispersão da largura e do comprimento das sépalas, distinguindo as espécies por cor.
3. **Visão 3:** Histograma da distribuição do comprimento das pétalas, separado por espécie.

---

## Como o sistema funciona

O programa exibe um menu interativo com as seguintes opções:

- 1. Ver resumo do dataset
- 2. Comparar o comprimento médio das pétalas por espécie
- 3. Gerar gráfico de dispersão das sépalas
- 4. Gerar histograma do comprimento das pétalas
- 5. Sair

Os gráficos são salvos na pasta `outputs/`. O arquivo `data/iris.csv` é o CSV `Iris.csv` do dataset Kaggle indicado acima.

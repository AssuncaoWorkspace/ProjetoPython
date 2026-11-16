
# Projeto: Análise de Dados com Python

**Disciplina:** Linguagem de Programação em Python (2026.2)  
**Professor:** Ruben Prado  
**Instituição:** Faculdade Senac-DF de Tecnologia e Inovação

---

## Objetivo do Projeto
Este projeto consolida os conhecimentos do semestre. A equipe atuou como Engenheiros de Dados para desenvolver um Sistema Analítico Interativo em CLI, responsável por ler uma base de dados, processá-la com Pandas, aplicar orientação a objetos e gerar insights visuais com Matplotlib e Seaborn.

---

## Estrutura do Repositório

```text
projeto-integrador-python/
│
├── data/
│   ├── dados_vendas.csv       # train.csv do Kaggle Superstore Sales Dataset
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
3. Geração de pelo menos 3 gráficos diferentes usando `groupby` ou filtros booleanos antes da plotagem.
4. Cada gráfico possui título e labels em x/y.

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

* **Tema Geral:** Vendas de uma loja global (Superstore)
* **Fonte de Dados (URL):** [Superstore Sales Dataset no Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
* **Arquivo utilizado:** `train.csv`, disponibilizado no Kaggle e armazenado como `data/dados_vendas.csv`. A base possui 9.800 registros e 18 colunas; a licença indicada na página do dataset é GPL-2.0.
* **Motivação:** A base contém vendas de produtos entre 2015 e 2018, com datas, produtos, categorias e segmentos de clientes. A análise investiga a evolução mensal da receita, os produtos com maior receita acumulada e a distribuição dos valores de venda por registro.

### 🏗️ Arquitetura e Estruturação

* **Módulos / Classes Criadas:** A classe `AnalisadorDeDados` em `src/analisador.py` centraliza a leitura do dataset, a limpeza dos dados e a geração dos gráficos.
* **Limpeza de Dados:** Os nomes das colunas são normalizados e os campos da análise são convertidos para tipos apropriados. As datas são interpretadas no formato dia/mês/ano; categorias textuais ausentes recebem rótulos explícitos e `dropna()` remove registros com data ou valor de venda inválido. Os 9.800 registros possuem valores válidos nos campos usados pela análise.
* **Nota sobre o dataset:** A base não contém coluna de quantidade vendida. Por isso, o sistema analisa valores de venda por registro e não apresenta métricas de quantidade.

### 📊 Gráficos Desenvolvidos

1. **Visão 1:** Gráfico de linha mostrando a evolução da receita mensal ao longo do tempo.
2. **Visão 2:** Gráfico de barras horizontais com os 5 produtos que mais geraram receita total.
3. **Visão 3:** Histograma da distribuição dos valores de venda por registro.

---

## Como o sistema funciona

O programa exibe um menu interativo com as seguintes opções:

- 1. Ver resumo do dataset
- 2. Gerar gráfico de linha
- 3. Gerar gráfico de barras
- 4. Gerar histograma
- 5. Sair

Os gráficos são salvos na pasta `outputs/` e podem ser consultados após a execução do programa. O CSV é o arquivo `train.csv` da fonte Kaggle indicada acima.

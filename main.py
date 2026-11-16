from pathlib import Path

from src.analisador import AnalisadorDeDados


def exibir_menu() -> None:
    print("\n=== Sistema Analítico de Dados ===")
    print("1. Ver resumo do dataset")
    print("2. Gerar gráfico de linha")
    print("3. Gerar gráfico de barras")
    print("4. Gerar histograma")
    print("5. Sair")


def main() -> None:
    caminho_csv = Path("data/dados_vendas.csv")
    analisador = AnalisadorDeDados(caminho_csv)

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 5.")
            continue

        if opcao == 1:
            print("\nResumo do dataset:")
            print(analisador.resumo_dados())
            print("\nPrimeiras linhas do dataframe:")
            print(analisador.mostrar_dados(5))

        elif opcao == 2:
            caminho = analisador.gerar_grafico_linha("outputs/grafico_linha.png")
            print(f"Gráfico de linha salvo em: {caminho}")

        elif opcao == 3:
            caminho = analisador.gerar_grafico_barras("outputs/grafico_barras.png")
            print(f"Gráfico de barras salvo em: {caminho}")

        elif opcao == 4:
            caminho = analisador.gerar_histograma("outputs/histograma_vendas.png")
            print(f"Histograma salvo em: {caminho}")

        elif opcao == 5:
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Selecione um número entre 1 e 5.")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
        print("Coloque o arquivo CSV em data/dados_vendas.csv antes de executar o sistema.")
    except ValueError as erro:
        print(f"Erro na leitura do dataset: {erro}")

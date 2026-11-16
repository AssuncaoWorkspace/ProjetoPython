from pathlib import Path

from src.analisador import AnalisadorDeDados


def exibir_menu() -> None:
    print("\n=== Análise de Dados das Flores Iris ===")
    print("1. Ver resumo do dataset")
    print("2. Comparar comprimento médio das pétalas por espécie")
    print("3. Gerar dispersão das medidas das sépalas")
    print("4. Gerar histograma do comprimento das pétalas")
    print("5. Sair")


def main() -> None:
    caminho_csv = Path("data/iris.csv")
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
            caminho = analisador.gerar_grafico_barras("outputs/media_petala_por_especie.png")
            print(f"Gráfico comparativo salvo em: {caminho}")

        elif opcao == 3:
            caminho = analisador.gerar_grafico_dispersao("outputs/dispersao_iris.png")
            print(f"Gráfico de dispersão salvo em: {caminho}")

        elif opcao == 4:
            caminho = analisador.gerar_histograma("outputs/distribuicao_petalas.png")
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
        print("Coloque o arquivo iris.csv na pasta data antes de executar o sistema.")
    except ValueError as erro:
        print(f"Erro na leitura do dataset: {erro}")

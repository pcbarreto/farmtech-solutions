import csv
import math
from pathlib import Path

# Dados organizados em vetores (listas paralelas)
culturas = []
figuras = []
medida1 = []
medida2 = []
produtos = []
dosagens_ml_m = []
ruas = []
metros_por_rua = []
areas_m2 = []
insumos_litros = []

ARQUIVO_CSV = Path(__file__).resolve().parents[1] / "dados" / "dados_farmtech.csv"


def ler_float(msg: str) -> float:
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if valor < 0:
                print("Digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def ler_int(msg: str) -> int:
    while True:
        try:
            valor = int(input(msg))
            if valor < 0:
                print("Digite um valor inteiro positivo.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def escolher_cultura() -> str:
    while True:
        print("\nEscolha a cultura:")
        print("1 - Milho (área em retângulo)")
        print("2 - Café (área em círculo)")
        op = input("Opção: ").strip()

        if op == "1":
            return "Milho"
        if op == "2":
            return "Café"
        print("Opção inválida.")


def escolher_produto(cultura: str) -> str:
    while True:
        print(f"\nProdutos para {cultura}:")
        if cultura == "Milho":
            print("1 - Fertilizante NPK")
            print("2 - Herbicida")
            op = input("Opção: ").strip()
            if op == "1":
                return "Fertilizante NPK"
            if op == "2":
                return "Herbicida"
        elif cultura == "Café":
            print("1 - Fosfato")
            print("2 - Fungicida")
            op = input("Opção: ").strip()
            if op == "1":
                return "Fosfato"
            if op == "2":
                return "Fungicida"

        print("Opção inválida.")


def calcular_area(cultura: str, m1: float, m2: float = 0.0):
    if cultura == "Milho":
        # Retângulo = comprimento x largura
        return "Retângulo", m1 * m2

    # Café em círculo = pi x raio²
    return "Círculo", math.pi * (m1 ** 2)


def calcular_insumo_total(dosagem: float, qtd_ruas: int, metragem_rua: float) -> float:
    total_metros = qtd_ruas * metragem_rua
    total_ml = dosagem * total_metros
    return total_ml / 1000.0


def coletar_registro():
    cultura = escolher_cultura()

    if cultura == "Milho":
        comprimento = ler_float("Comprimento do talhão (m): ")
        largura = ler_float("Largura do talhão (m): ")
        fig, area = calcular_area(cultura, comprimento, largura)
        m1, m2 = comprimento, largura
    else:
        raio = ler_float("Raio da área plantada (m): ")
        fig, area = calcular_area(cultura, raio)
        m1, m2 = raio, 0.0

    produto = escolher_produto(cultura)
    dosagem = ler_float("Dosagem do produto (mL por metro): ")
    qtd_ruas = ler_int("Quantidade de ruas da lavoura: ")
    metragem_rua = ler_float("Metragem de cada rua (m): ")
    total_litros = calcular_insumo_total(dosagem, qtd_ruas, metragem_rua)

    return cultura, fig, m1, m2, produto, dosagem, qtd_ruas, metragem_rua, area, total_litros


def salvar_registro(registro, posicao=None):
    if posicao is None:
        culturas.append(registro[0])
        figuras.append(registro[1])
        medida1.append(registro[2])
        medida2.append(registro[3])
        produtos.append(registro[4])
        dosagens_ml_m.append(registro[5])
        ruas.append(registro[6])
        metros_por_rua.append(registro[7])
        areas_m2.append(registro[8])
        insumos_litros.append(registro[9])
    else:
        culturas[posicao] = registro[0]
        figuras[posicao] = registro[1]
        medida1[posicao] = registro[2]
        medida2[posicao] = registro[3]
        produtos[posicao] = registro[4]
        dosagens_ml_m[posicao] = registro[5]
        ruas[posicao] = registro[6]
        metros_por_rua[posicao] = registro[7]
        areas_m2[posicao] = registro[8]
        insumos_litros[posicao] = registro[9]


def cadastrar_dados():
    registro = coletar_registro()
    salvar_registro(registro)
    print("\nRegistro cadastrado com sucesso!")


def listar_dados():
    if not culturas:
        print("\nNenhum dado cadastrado.")
        return

    print("\n===== DADOS CADASTRADOS =====")
    for i in range(len(culturas)):
        print(f"\nPosição: {i}")
        print(f"Cultura: {culturas[i]}")
        print(f"Figura geométrica: {figuras[i]}")
        if culturas[i] == "Milho":
            print(f"Comprimento: {medida1[i]:.2f} m")
            print(f"Largura: {medida2[i]:.2f} m")
        else:
            print(f"Raio: {medida1[i]:.2f} m")
        print(f"Área plantada: {areas_m2[i]:.2f} m²")
        print(f"Produto: {produtos[i]}")
        print(f"Dosagem: {dosagens_ml_m[i]:.2f} mL/m")
        print(f"Ruas: {ruas[i]}")
        print(f"Metros por rua: {metros_por_rua[i]:.2f} m")
        print(f"Insumo total necessário: {insumos_litros[i]:.2f} L")


def atualizar_dados():
    if not culturas:
        print("\nNão há dados para atualizar.")
        return

    listar_dados()
    pos = ler_int("\nInforme a posição que deseja atualizar: ")

    if pos < 0 or pos >= len(culturas):
        print("Posição inválida.")
        return

    print("\nDigite os novos dados do registro:")
    novo_registro = coletar_registro()
    salvar_registro(novo_registro, pos)
    print("\nRegistro atualizado com sucesso!")


def deletar_dados():
    if not culturas:
        print("\nNão há dados para excluir.")
        return

    listar_dados()
    pos = ler_int("\nInforme a posição que deseja excluir: ")

    if pos < 0 or pos >= len(culturas):
        print("Posição inválida.")
        return

    culturas.pop(pos)
    figuras.pop(pos)
    medida1.pop(pos)
    medida2.pop(pos)
    produtos.pop(pos)
    dosagens_ml_m.pop(pos)
    ruas.pop(pos)
    metros_por_rua.pop(pos)
    areas_m2.pop(pos)
    insumos_litros.pop(pos)

    print("\nRegistro removido com sucesso!")


def exportar_csv():
    if not culturas:
        print("\nNenhum dado cadastrado para exportar.")
        return

    ARQUIVO_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "cultura",
            "figura",
            "medida1",
            "medida2",
            "produto",
            "dosagem_ml_m",
            "ruas",
            "metros_por_rua",
            "area_m2",
            "insumo_total_litros",
        ])

        for i in range(len(culturas)):
            writer.writerow([
                culturas[i],
                figuras[i],
                medida1[i],
                medida2[i],
                produtos[i],
                dosagens_ml_m[i],
                ruas[i],
                metros_por_rua[i],
                areas_m2[i],
                insumos_litros[i],
            ])

    print(f"\nArquivo exportado com sucesso em: {ARQUIVO_CSV}")


def menu():
    while True:
        print("\n======= MENU FARMTECH SOLUTIONS =======")
        print("1 - Entrada de dados")
        print("2 - Saída de dados")
        print("3 - Atualização de dados em uma posição do vetor")
        print("4 - Deleção de dados do vetor")
        print("5 - Exportar dados para CSV")
        print("6 - Sair do programa")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            exportar_csv()
        elif opcao == "6":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

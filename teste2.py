import random
import sys
from typing import Tuple


def linha():
    print("\n" + "-" * 50 + "\n")


def perguntar_sim_nao(pergunta: str) -> bool:
    while True:
        resp = input(pergunta + " (s/n): ").strip().lower()
        if resp in ("s", "sim"):  # Sim
            return True
        if resp in ("n", "nao", "não"):  # Não
            return False
        print("Opção inválida. Tente novamente.")


def obter_int(pergunta: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        valor = input(pergunta).strip()
        if not valor.isdigit():
            print("Digite um número inteiro válido.")
            continue
        num = int(valor)
        if minimo is not None and num < minimo:
            print(f"O número deve ser >= {minimo}.")
            continue
        if maximo is not None and num > maximo:
            print(f"O número deve ser <= {maximo}.")
            continue
        return num


def jogo_adivinhacao() -> None:
    linha()
    print("Jogo: Adivinhe o Número")
    print("Eu vou pensar em um número e você tentará adivinhar!")

    limite_inferior = 1
    limite_superior = 100
    numero_secreto = random.randint(limite_inferior, limite_superior)

    print(f"Pensei em um número entre {limite_inferior} e {limite_superior}.")
    tentativas_max = 10
    print(f"Você tem {tentativas_max} tentativas. Boa sorte!")

    for tentativa in range(1, tentativas_max + 1):
        palpite = obter_int(f"Tentativa {tentativa}/{tentativas_max} - Seu palpite: ", limite_inferior, limite_superior)

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número!")
            print(f"Você precisou de {tentativa} tentativa(s).")
            break
        elif palpite < numero_secreto:
            print("Quase! O número é MAIOR.")
        else:
            print("Quase! O número é MENOR.")
    else:
        print("\nQue pena! Suas tentativas acabaram.")
        print(f"O número secreto era: {numero_secreto}")

    linha()
    input("Pressione ENTER para voltar ao menu...")


def calcular_vencedor_rps(jogador: str, computador: str) -> int:
    # Retorna: 1 se jogador vence, -1 se perde, 0 se empata
    regras = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel",
    }
    if jogador == computador:
        return 0
    return 1 if regras[jogador] == computador else -1


def escolher_opcao_rps(pergunta: str) -> str:
    opcoes = {"1": "pedra", "2": "papel", "3": "tesoura"}
    while True:
        print("\nEscolha sua jogada:")
        print("1) Pedra")
        print("2) Papel")
        print("3) Tesoura")
        escolha = input(pergunta).strip()
        if escolha in opcoes:
            return opcoes[escolha]
        if escolha.lower() in ("pedra", "papel", "tesoura"):
            return escolha.lower()
        print("Opção inválida. Tente novamente.")


def jogo_pedra_papel_tesoura() -> None:
    linha()
    print("Jogo: Pedra, Papel, Tesoura")
    print("Vença o computador em uma melhor de 5 rodadas!")

    vitorias = 0
    derrotas = 0
    empates = 0

    rodadas = 5
    opcoes = ["pedra", "papel", "tesoura"]

    for r in range(1, rodadas + 1):
        print(f"\nRodada {r}/{rodadas}")
        jogador = escolher_opcao_rps(
            "Sua escolha (1-3 ou digite pedra/papel/tesoura): "
        )
        computador = random.choice(opcoes)
        print(f"Você jogou: {jogador} | Computador jogou: {computador}")

        resultado = calcular_vencedor_rps(jogador, computador)
        if resultado == 1:
            print("Você venceu a rodada!")
            vitorias += 1
        elif resultado == -1:
            print("Você perdeu a rodada.")
            derrotas += 1
        else:
            print("Rodada empatada.")
            empates += 1

    linha()
    print("Placar final:")
    print(f"Vitórias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

    if vitorias > derrotas:
        print("Parabéns! Você venceu o jogo!")
    elif vitorias < derrotas:
        print("O computador venceu. Tente novamente!")
    else:
        print("Empate geral!")

    linha()
    input("Pressione ENTER para voltar ao menu...")


def mostrar_menu() -> None:
    linha()
    print("Bem-vindo ao Mini Arcade Python! 🎮")
    print("Escolha um jogo para começar:")
    print("1) Adivinhe o Número")
    print("2) Pedra, Papel, Tesoura")
    print("3) Sair")


def menu() -> None:
    while True:
        mostrar_menu()
        opcao = input("Sua opção: ").strip()
        if opcao == "1":
            jogo_adivinhacao()
        elif opcao == "2":
            jogo_pedra_papel_tesoura()
        elif opcao == "3":
            print("Até a próxima! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEncerrando. Até logo!")
        sys.exit(0)
bojekefugsdubiishubaiu

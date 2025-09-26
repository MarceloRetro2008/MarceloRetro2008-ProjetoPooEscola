import os
import sys
import time


# ==========================
#  Motor simples de Visual Novel (console)
# ==========================
TYPE_SPEED = 0.015  # menor = mais rápido; 0 para sem efeito de máquina de escrever


def clear():
    """Limpa a tela do console (Windows/Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def typewriter(text: str, speed: float = TYPE_SPEED):
    """Imprime o texto com efeito de máquina de escrever."""
    if speed <= 0:
        print(text)
        return
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(speed)
    print()


def say(speaker: str, text: str, speed: float = TYPE_SPEED):
    """Mostra a fala de um personagem."""
    if speaker:
        prefix = f"{speaker}: "
    else:
        prefix = ""
    typewriter(prefix + text, speed)


def pause(msg: str = "[Enter para continuar]"):
    try:
        input(msg)
    except EOFError:
        # Em alguns ambientes sem stdin, apenas espera um pouco
        time.sleep(0.5)


def choice(options):
    """Exibe opções e retorna o índice escolhido (0..n-1)."""
    while True:
        for i, opt in enumerate(options, start=1):
            print(f"{i}) {opt}")
        sel = input("> ").strip()
        if sel.isdigit():
            idx = int(sel) - 1
            if 0 <= idx < len(options):
                return idx
        print("Opção inválida. Tente novamente.")


# ==========================
#  História: Conhecendo Do Vale e JL
# ==========================


def titulo():
    clear()
    print("=" * 50)
    print(" Visual Novel: Encontro no Corredor ")
    print("=" * 50)
    print()
    typewriter("Do Vale e JL estão no corredor da escola.")
    typewriter("Hoje, você vai conhecê-los.")
    print()
    pause()


def introducao(player_name: str):
    clear()
    say("Narrador", f"{player_name}, é hora do intervalo. O corredor está cheio de alunos.")
    say("Narrador", "Você avista duas figuras conhecidas: Do Vale, concentrado em um cartaz do clube, e JL, animado conversando com um grupo.")
    print()


def cena_corredor(player_name: str):
    say("Narrador", "Quem você quer abordar primeiro?")
    op = choice(["Falar com Do Vale", "Falar com JL", "Ficar observando de longe"])
    if op == 0:
        return caminho_do_vale(player_name)
    elif op == 1:
        return caminho_jl(player_name)
    else:
        return caminho_observador(player_name)


def caminho_do_vale(player_name: str):
    clear()
    say("Narrador", "Você se aproxima de Do Vale. Ele percebe sua presença e sorri de leve.")
    say("Do Vale", "Oi. Você viu o cartaz do clube? Estamos procurando novas ideias.")
    say("Narrador", "Como você responde?")
    op = choice([
        "Oferecer ajuda com ideias para o clube",
        "Perguntar mais sobre o que ele gosta",
        "Dizer que está com pressa e sair",
    ])
    if op == 0:
        say(player_name, "Eu adoraria ajudar! Tenho algumas ideias criativas.")
        say("Do Vale", "Sério? Isso é ótimo. Podemos nos reunir depois da aula.")
        say("Narrador", "Vocês trocam contatos e marcam uma conversa. Uma nova parceria começa.")
        return final_amizade("Do Vale")
    elif op == 1:
        say(player_name, "O que você curte fazer no clube?")
        say("Do Vale", "Gosto de organizar projetos e ver tudo funcionando. É satisfatório.")
        say("Narrador", "Vocês conversam por um tempo e descobrem interesses em comum.")
        return final_neutro("Do Vale")
    else:
        say(player_name, "Desculpa, lembrei de um compromisso. Até mais!")
        say("Do Vale", "Sem problemas. Até.")
        say("Narrador", "Você se afasta, sentindo que perdeu uma oportunidade.")
        return final_distante("Do Vale")


def caminho_jl(player_name: str):
    clear()
    say("Narrador", "Você se aproxima de JL, que está rindo de uma piada.")
    say("JL", "E aí! Chegou na hora certa. Vamos fazer algo depois da aula?")
    say("Narrador", "Qual a sua reação?")
    op = choice([
        "Aceitar e sugerir um jogo/atividade",
        "Perguntar sobre os interesses de JL",
        "Recusar educadamente",
    ])
    if op == 0:
        say(player_name, "Topo! Que tal um jogo rápido ou um projeto divertido?")
        say("JL", "Perfeito! Adoro essa energia. Fechado!")
        say("Narrador", "Vocês combinam detalhes e parecem se dar muito bem.")
        return final_amizade("JL")
    elif op == 1:
        say(player_name, "O que você curte fazer no tempo livre?")
        say("JL", "Eu gosto de juntar a galera e testar ideias novas. É sempre animado!")
        say("Narrador", "A conversa flui leve e descontraída.")
        return final_neutro("JL")
    else:
        say(player_name, "Pô, hoje não vou conseguir. Mas valeu o convite!")
        say("JL", "Tranquilo! Fica pra próxima.")
        say("Narrador", "Você se despede, mas sente que poderia ter sido diferente.")
        return final_distante("JL")


def caminho_observador(player_name: str):
    clear()
    say("Narrador", "Você decide observar um pouco. A movimentação do corredor te distrai.")
    say("Narrador", "Quando percebe, o sinal toca e todos começam a se dispersar.")
    say("Narrador", "Ainda dá tempo para uma atitude.")
    op = choice(["Ir até Do Vale antes da aula", "Caminhar até JL rapidamente", "Deixar para outro dia"])
    if op == 0:
        return caminho_do_vale(player_name)
    elif op == 1:
        return caminho_jl(player_name)
    else:
        say("Narrador", "Você respira fundo e decide esperar. Talvez amanhã.")
        return final_reflexivo()


# ==========================
#  Finais
# ==========================


def final_amizade(personagem: str):
    print()
    say("Final", f"Uma nova amizade com {personagem} floresce.")
    say("Final", "Vocês planejam algo juntos e a história está só começando.")
    return "Amizade"


def final_neutro(personagem: str):
    print()
    say("Final", f"Você e {personagem} se conhecem melhor. O futuro é promissor.")
    return "Neutro"


def final_distante(personagem: str):
    print()
    say("Final", f"{personagem} ficou um pouco distante. Talvez outra oportunidade apareça.")
    return "Distante"


def final_reflexivo():
    print()
    say("Final", "Você escolhe esperar. Às vezes, o momento certo ainda vai chegar.")
    return "Reflexivo"


# ==========================
#  Loop principal
# ==========================


def main():
    titulo()
    clear()
    print("Configurações rápidas:")
    print("1) Texto normal (efeito de digitação)")
    print("2) Texto rápido (sem efeito)")
    modo = input("> ").strip()
    global TYPE_SPEED
    if modo == "2":
        TYPE_SPEED = 0

    clear()
    player_name = input("Seu nome: ").strip() or "Você"
    introducao(player_name)
    fim = cena_corredor(player_name)

    print()
    print("=" * 50)
    print(f"FIM - Rota: {fim}")
    print("=" * 50)
    print()
    say("Narrador", "Deseja jogar novamente?")
    if choice(["Sim", "Não"]) == 0:
        main()
    else:
        say("Narrador", "Obrigado por jogar!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")


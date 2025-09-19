import json
import os
import re
from datetime import datetime
from getpass import getpass


USERS_FILE = "usuarios.json"


def validar_nome(nome: str) -> bool:
    return bool(nome.strip()) and len(nome.strip()) >= 2


def validar_email(email: str) -> bool:
    # Regex simples e prática para validar emails comuns
    padrao = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None


def limpar_cpf(cpf: str) -> str:
    return re.sub(r"\D", "", cpf)


def validar_cpf(cpf: str) -> bool:
    # Validação de CPF com dígitos verificadores
    cpf = limpar_cpf(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_dv(cpf_parcial: str) -> int:
        soma = sum(int(d) * m for d, m in zip(cpf_parcial, range(len(cpf_parcial) + 1, 1, -1)))
        resto = soma % 11
        dv = 0 if resto < 2 else 11 - resto
        return dv

    dv1 = calc_dv(cpf[:9])
    dv2 = calc_dv(cpf[:9] + str(dv1))
    return cpf.endswith(f"{dv1}{dv2}")


def validar_data(data_str: str) -> bool:
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        # Não permitir datas futuras
        return data <= datetime.now()
    except ValueError:
        return False


def validar_telefone(tel: str) -> bool:
    # Aceita formatos com DDD e 8-9 dígitos, ignorando caracteres não numéricos
    numeros = re.sub(r"\D", "", tel)
    return 10 <= len(numeros) <= 11


def ler_entrada(prompt: str, validador, transform=None, erro: str = "Entrada inválida. Tente novamente."):
    while True:
        valor = input(prompt).strip()
        if transform:
            valor_transformado = transform(valor)
        else:
            valor_transformado = valor
        if validador(valor_transformado):
            return valor_transformado
        print(erro)


def salvar_usuario(dados: dict, caminho: str = USERS_FILE) -> None:
    # Carrega arquivo existente ou inicia lista vazia
    registros = []
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                registros = json.load(f) or []
        except json.JSONDecodeError:
            # Se arquivo estiver corrompido, recomeça
            registros = []

    registros.append(dados)

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)


def cadastrar_usuario():
    print("\n===== Cadastro de Usuário =====")

    nome = ler_entrada(
        "Nome completo: ",
        validar_nome,
        erro="Nome deve ter pelo menos 2 caracteres."
    )

    email = ler_entrada(
        "E-mail: ",
        validar_email,
        erro="E-mail inválido. Ex: usuario@dominio.com"
    )

    cpf = ler_entrada(
        "CPF (somente números ou com pontuação): ",
        validar_cpf,
        transform=limpar_cpf,
        erro="CPF inválido. Verifique e tente novamente."
    )

    data_nascimento = ler_entrada(
        "Data de nascimento (DD/MM/AAAA): ",
        validar_data,
        erro="Data inválida. Use o formato DD/MM/AAAA e não informe data futura."
    )

    telefone = ler_entrada(
        "Telefone (com DDD): ",
        validar_telefone,
        erro="Telefone inválido. Informe 10 ou 11 dígitos (com DDD)."
    )

    # Senha com confirmação (entrada oculta)
    while True:
        senha = getpass("Senha (mín. 6 caracteres): ")
        if len(senha) < 6:
            print("A senha deve ter pelo menos 6 caracteres.")
            continue
        confirma = getpass("Confirme a senha: ")
        if senha != confirma:
            print("As senhas não conferem. Tente novamente.")
            continue
        break

    usuario = {
        "nome": nome,
        "email": email.lower(),
        "cpf": cpf,  # armazenado apenas com números
        "data_nascimento": data_nascimento,
        "telefone": re.sub(r"\D", "", telefone),
        "criado_em": datetime.now().isoformat(timespec="seconds"),
    }

    salvar_usuario(usuario)

    print("\nCadastro realizado com sucesso!")
    print("Dados salvos em:", os.path.abspath(USERS_FILE))


def listar_usuarios(caminho: str = USERS_FILE):
    print("\n===== Usuários Cadastrados =====")
    if not os.path.exists(caminho):
        print("Nenhum usuário cadastrado ainda.")
        return
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            registros = json.load(f) or []
    except json.JSONDecodeError:
        print("Arquivo de usuários está corrompido ou vazio.")
        return

    if not registros:
        print("Nenhum usuário cadastrado ainda.")
        return

    for i, u in enumerate(registros, start=1):
        print(f"{i}. {u.get('nome')} | {u.get('email')} | CPF: {u.get('cpf')} | Nasc: {u.get('data_nascimento')} | Tel: {u.get('telefone')}")


def menu():
    while True:
        print("\n===== Menu =====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
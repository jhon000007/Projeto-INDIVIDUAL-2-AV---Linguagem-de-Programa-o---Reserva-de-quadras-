import json
from datetime import datetime, date
from pathlib import Path

VALOR_POR_HORA = 85.00

ARQUIVO = Path(__file__).with_name("dados_arena.json")


def carregar_dados():
    if ARQUIVO.exists():
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
        except (json.JSONDecodeError, OSError):
            print("Não foi possível ler os dados. Um arquivo novo será criado.")

    return {"clientes": [], "reservas": []}


def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def ler_data(mensagem):
    while True:
        texto = input(mensagem)
        try:
            return datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")


def buscar_cliente(id_cliente):
    for cliente in dados["clientes"]:
        if cliente["id"] == id_cliente:
            return cliente
    return None


def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()

    if not nome or not telefone:
        print("Nome e telefone são obrigatórios.")
        return

    novo_id = max([c["id"] for c in dados["clientes"]], default=0) + 1
    dados["clientes"].append({
        "id": novo_id,
        "nome": nome,
        "telefone": telefone
    })
    salvar_dados()
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\n--- CLIENTES ---")
    if not dados["clientes"]:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in dados["clientes"]:
        print(f'ID: {cliente["id"]} | Nome: {cliente["nome"]} | Telefone: {cliente["telefone"]}')


def alterar_cliente():
    listar_clientes()
    if not dados["clientes"]:
        return

    try:
        id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))
    except ValueError:
        print("ID inválido.")
        return

    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    nome = input(f'Novo nome [{cliente["nome"]}]: ').strip()
    telefone = input(f'Novo telefone [{cliente["telefone"]}]: ').strip()

    if nome:
        cliente["nome"] = nome
    if telefone:
        cliente["telefone"] = telefone

    salvar_dados()
    print("Cliente alterado com sucesso!")


def excluir_cliente():
    listar_clientes()
    if not dados["clientes"]:
        return

    try:
        id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    hoje = date.today().isoformat()
    tem_reserva_futura = any(
        r["cliente_id"] == id_cliente and r["data"] >= hoje
        for r in dados["reservas"]
    )

    if tem_reserva_futura:
        print("Não é possível excluir: este cliente possui reservas futuras.")
        return

    dados["clientes"].remove(cliente)
    salvar_dados()
    print("Cliente excluído com sucesso!")


def horarios_ocupados(data_reserva):
    ocupados = set()

    for reserva in dados["reservas"]:
        if reserva["data"] == data_reserva:
            inicio = reserva["inicio"]
            fim = inicio + reserva["duracao"]
            for hora in range(inicio, fim):
                ocupados.add(hora)

    return ocupados


def consultar_agenda():
    print("\n--- CONSULTAR AGENDA ---")
    data_reserva = ler_data("Data (DD/MM/AAAA): ").isoformat()
    ocupados = horarios_ocupados(data_reserva)

    print(f"\nAgenda do dia {datetime.strptime(data_reserva, '%Y-%m-%d').strftime('%d/%m/%Y')}")
    for hora in range(8, 23):
        situacao = "OCUPADO" if hora in ocupados else "LIVRE"
        print(f"{hora:02d}:00 - {situacao}")


def reservar_quadra():
    print("\n--- RESERVAR QUADRA ---")
    listar_clientes()
    if not dados["clientes"]:
        print("Cadastre um cliente antes de fazer uma reserva.")
        return

    try:
        id_cliente = int(input("ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return

    cliente = buscar_cliente(id_cliente)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    data_escolhida = ler_data("Data da reserva (DD/MM/AAAA): ")
    if data_escolhida < date.today():
        print("Não é possível reservar uma data que já passou.")
        return

    data_reserva = data_escolhida.isoformat()
    ocupados = horarios_ocupados(data_reserva)

    print("\nHorários disponíveis:")
    for hora in range(8, 23):
        if hora not in ocupados:
            print(f"{hora:02d}:00", end="  ")
    print()

    try:
        inicio = int(input("Horário inicial (somente a hora, de 8 a 22): "))
        duracao = int(input("Quantidade de horas: "))
    except ValueError:
        print("Digite números válidos.")
        return

    if inicio < 8 or inicio > 22:
        print("O horário inicial deve ser entre 08:00 e 22:00.")
        return

    if duracao < 1:
        print("A reserva deve ter pelo menos 1 hora.")
        return

    if inicio + duracao > 23:
        print("A reserva não pode ultrapassar as 23:00.")
        return

    for hora in range(inicio, inicio + duracao):
        if hora in ocupados:
            print(f"O horário {hora:02d}:00 já está ocupado.")
            return

    valor = VALOR_POR_HORA * duracao
    novo_id = max([r["id"] for r in dados["reservas"]], default=0) + 1

    dados["reservas"].append({
        "id": novo_id,
        "cliente_id": id_cliente,
        "data": data_reserva,
        "inicio": inicio,
        "duracao": duracao,
        "valor": valor
    })

    salvar_dados()
    print("\nReserva realizada com sucesso!")
    print(f"Cliente: {cliente['nome']}")
    print(f"Horário: {inicio:02d}:00 até {inicio + duracao:02d}:00")
    print(f"Valor: R$ {valor:.2f}")


def cancelar_reserva():
    print("\n--- CANCELAR RESERVA ---")
    data_reserva = ler_data("Data da reserva (DD/MM/AAAA): ").isoformat()

    reservas_do_dia = [
        r for r in dados["reservas"] if r["data"] == data_reserva
    ]

    if not reservas_do_dia:
        print("Não existem reservas nessa data.")
        return

    for reserva in reservas_do_dia:
        cliente = buscar_cliente(reserva["cliente_id"])
        nome = cliente["nome"] if cliente else "Cliente não encontrado"
        fim = reserva["inicio"] + reserva["duracao"]
        print(
            f'ID: {reserva["id"]} | {nome} | '
            f'{reserva["inicio"]:02d}:00 até {fim:02d}:00 | '
            f'R$ {reserva["valor"]:.2f}'
        )

    try:
        id_reserva = int(input("ID da reserva que deseja cancelar: "))
    except ValueError:
        print("ID inválido.")
        return

    for reserva in dados["reservas"]:
        if reserva["id"] == id_reserva and reserva["data"] == data_reserva:
            confirmacao = input("Confirma o cancelamento? (S/N): ").strip().upper()
            if confirmacao == "S":
                dados["reservas"].remove(reserva)
                salvar_dados()
                print("Reserva cancelada. Horários liberados.")
            else:
                print("Cancelamento não realizado.")
            return

    print("Reserva não encontrada.")


def relatorio_faturamento():
    print("\n--- RELATÓRIO DE FATURAMENTO ---")
    inicio = ler_data("Data inicial (DD/MM/AAAA): ")
    fim = ler_data("Data final (DD/MM/AAAA): ")

    if fim < inicio:
        print("A data final não pode ser anterior à data inicial.")
        return

    total = 0
    quantidade = 0

    for reserva in dados["reservas"]:
        data_reserva = date.fromisoformat(reserva["data"])
        if inicio <= data_reserva <= fim:
            total += reserva["valor"]
            quantidade += 1

    print(f"Quantidade de reservas: {quantidade}")
    print(f"Faturamento do período: R$ {total:.2f}")


def menu():
    while True:
        print("\n========== ARENA SEBASTIÃO ==========")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Alterar cliente")
        print("4 - Excluir cliente")
        print("5 - Consultar agenda")
        print("6 - Reservar quadra")
        print("7 - Cancelar reserva")
        print("8 - Relatório de faturamento")
        print("0 - Sair")
        print("=====================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            alterar_cliente()
        elif opcao == "4":
            excluir_cliente()
        elif opcao == "5":
            consultar_agenda()
        elif opcao == "6":
            reservar_quadra()
        elif opcao == "7":
            cancelar_reserva()
        elif opcao == "8":
            relatorio_faturamento()
        elif opcao == "0":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


dados = carregar_dados()
menu()

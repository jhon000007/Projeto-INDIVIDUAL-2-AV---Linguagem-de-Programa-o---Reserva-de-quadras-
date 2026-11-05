# Reserva de quadra - sistema para UMA quadra (Arena Sebastião)
# Cada horário dura 1 hora (mínimo). Dá para reservar várias horas seguidas.

from datetime import date

# ----- DADOS FIXOS -----
# Troque o valor pelo preço real por hora da quadra.
QUADRA = {"nome": "Arena Sebastião", "valor_hora": 80.0}

# Horários de início: 08:00, 09:00, ..., 22:00 (ajuste ao funcionamento real)
HORARIOS = [f"{h:02d}:00" for h in range(8, 23)]

ARQUIVO = "reservas.txt"  # fica na pasta de onde o programa é executado

# ----- DADOS QUE MUDAM -----
reservas = []  # {"id", "cliente", "data", "hora", "duracao", "valor"}


# ----- SUBPROGRAMAS -----
def salvar():
    """Grava todas as reservas no arquivo, uma por linha, campos separados por |."""
    with open(ARQUIVO, "w", encoding="utf-8") as arq:
        for r in reservas:
            campos = [str(r["id"]), r["cliente"], r["data"], r["hora"],
                      str(r["duracao"]), str(r["valor"])]
            arq.write("|".join(campos) + "\n")


def carregar():
    """Lê o arquivo (se existir) e recria a lista de reservas."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if linha == "":
                    continue
                i, cli, data, hora, dur, valor = linha.split("|")
                reservas.append({"id": int(i), "cliente": cli, "data": data,
                                 "hora": hora, "duracao": int(dur),
                                 "valor": float(valor)})
    except FileNotFoundError:
        pass  # primeira execução: o arquivo ainda não existe


def proximo_id():
    maior = 0
    for r in reservas:
        if r["id"] > maior:
            maior = r["id"]
    return maior + 1


def converter_data(texto):
    """Transforma 'dd/mm/aaaa' em date. Devolve None se for inválida."""
    partes = texto.split("/")
    if len(partes) != 3:
        return None
    for p in partes:
        if not p.isdigit():
            return None
    try:
        return date(int(partes[2]), int(partes[1]), int(partes[0]))
    except ValueError:  # ex.: 31/02/2030
        return None


def reserva_no_horario(data, hora):
    """Devolve a reserva que ocupa aquele horário naquela data, ou None."""
    for r in reservas:
        inicio = HORARIOS.index(r["hora"])
        if r["data"] == data and hora in HORARIOS[inicio:inicio + r["duracao"]]:
            return r
    return None


def mostrar_horarios(data):
    print(f'\nHorários de {QUADRA["nome"]} em {data} (cada um = 1 hora):')
    for i, h in enumerate(HORARIOS):
        r = reserva_no_horario(data, h)
        if r is None:
            print(f"{i + 1:2d} - {h}  livre")
        else:
            print(f'{i + 1:2d} - {h}  OCUPADO ({r["cliente"]})')


def reservar():
    cliente = input("Nome do cliente: ").strip().title().replace("|", "")
    if cliente == "":
        print("Informe o nome do cliente.")
        return

    dia = converter_data(input("Data (dd/mm/aaaa): ").strip())
    if dia is None:
        print("Data inválida.")
        return
    if dia < date.today():
        print("Essa data já passou.")
        return
    data = dia.strftime("%d/%m/%Y")  # guarda sempre no mesmo formato

    mostrar_horarios(data)
    escolha = input("Número do horário inicial: ").strip()
    horas_txt = input("Quantas horas (mínimo 1): ").strip()
    if not escolha.isdigit() or not horas_txt.isdigit():
        print("Digite apenas números.")
        return

    inicio = int(escolha) - 1
    duracao = int(horas_txt)
    if duracao < 1:
        print("O mínimo é 1 hora.")
        return
    if inicio < 0 or inicio + duracao > len(HORARIOS):
        print("Horário fora do funcionamento.")
        return

    for h in HORARIOS[inicio:inicio + duracao]:
        if reserva_no_horario(data, h) is not None:
            print(f"O horário {h} já está reservado!")
            return

    valor = QUADRA["valor_hora"] * duracao
    reservas.append({
        "id": proximo_id(),
        "cliente": cliente,
        "data": data,
        "hora": HORARIOS[inicio],
        "duracao": duracao,
        "valor": valor,
    })
    salvar()
    print(f"Reservado! {data} às {HORARIOS[inicio]} por {duracao}h - total R$ {valor:.2f}")


def ver_agenda():
    dia = converter_data(input("Data (dd/mm/aaaa): ").strip())
    if dia is None:
        print("Data inválida.")
        return
    mostrar_horarios(dia.strftime("%d/%m/%Y"))


def cancelar():
    if len(reservas) == 0:
        print("Não há reservas.")
        return
    for r in reservas:
        print(f'{r["id"]} - {r["data"]} {r["hora"]} ({r["duracao"]}h) - {r["cliente"]}')
    codigo = input("Id da reserva a cancelar: ").strip()
    for r in reservas:
        if codigo == str(r["id"]):
            reservas.remove(r)
            salvar()
            print("Reserva cancelada.")
            return
    print("Id não encontrado.")


# ----- MENU PRINCIPAL -----
carregar()  # recupera as reservas salvas ao abrir o programa

while True:
    print(f'\n=== {QUADRA["nome"]} ===')
    print("1 - Nova reserva\n2 - Ver agenda do dia\n3 - Cancelar reserva\n0 - Sair")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        reservar()
    elif opcao == "2":
        ver_agenda()
    elif opcao == "3":
        cancelar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")

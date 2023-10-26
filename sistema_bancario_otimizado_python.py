import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print("\n Operação falhou! sem saldo suficiente")
    
    elif limite_excedido:
        print("\n Operação falhou! valor de saque acima do limite permitido")

    elif saque_excedido:
        print("\n Operação falhou! número de saques máximos excedido")
        
    elif valor > 0:
        saldo = saldo - valor
        extrato = extrato + f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques = numero_saques + 1
        print("\n=== Saque realizado com sucesso! ===")
    
    else:
        print("\n Operação falhou! valor informado é inválido")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f"Depósito: \tR$ {valor:.2f}\n"
        print("\n Depósito foi realizado")
    else:
        print("\n Ocorreu um erro! operação falhou.")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, operação encerrada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)   

def main():
    menu = """
         MENU
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair
    => """

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":
            limpar_tela()
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            limpar_tela()
            valor = float(input("Informe o valor a ser retirado: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            limpar_tela()
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            limpar_tela()
            criar_usuario(usuarios)

        elif opcao == "5":
            limpar_tela()
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            limpar_tela()
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, tente novamente")
        
main()

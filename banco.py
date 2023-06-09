from typing import List
from time import sleep
from conta import Conta
from cliente import Cliente


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=====================================')
    print('================ ATM ================')
    print('============ Samuel Bank ============')
    print('=====================================')
    print('Selecione um opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sitema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte Sempre!!')
        sleep(2)
        exit(0)
    else:
        print('Opção Invalida')
        sleep(2)
        menu()


def criar_conta() -> None:

    print('Informe os dados do cliente: ')

    nome: str = input('Informe o nome do cliente: ')
    email: str = input('Informe email do cliente: ')
    cpf: str = input('Infome o cpf do cliente: ')
    data_nascimento: str = input('Informe a data de nascimento do cliente (dd/mm/aaaa): ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados do conta: ')
    print('=========================')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com numero {numero}')

    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do deposito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com numero {numero}')

    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o numero da sua conta: '))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if numero_o:
            numero_d: int = int(input('Informe o numero da conta destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if numero_d:
                valor: int = int(input('Informe o valor da transferencia: '))
                conta_o.transferir(conta_d, valor)

            else:
                print(f'Sua destino com numero {numero_o} não foi encontrada.')

        else:
            print(f'Sua conta com numero {numero_o} não foi encontrada.')

    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('======================')
            sleep(2)
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if numero == conta.numero:
                c = conta
    return c


if __name__ == '__main__':
    main()



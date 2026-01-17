import os

from cliente import Cliente

from conta  import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

from banco import Banco

cliente_sessao = 0
idCliente = 0
lista_clientes = []
lista_bancos = [
    (999, Banco(999,"Caixa")),
    (1, Banco(1,"Brasil")),
    (237, Banco(237,"Bradesco")),
    (33, Banco(33,"Santander")),
    (341, Banco(341,"Itau")),
]

MENU = """
--------------------------------------
---------- SISTEMA BANCARIO ----------
--------------------------------------

-- (1) Cadastrar-se
-- (2) Criar Conta
-- (3) Entrar na conta

-- (0) Sair
"""

def validaCliente():
    global cliente_sessao

    print("\nVocê já está cadastrado como cliente? S/N")
    opcao = input("\n=>").upper()
    
    if opcao not in ('S', 'N'):
        os.system("clear")
        print("Opção selecionada não reconhecida !!")
        return False
    
    if opcao == 'N':
        cadastrarCliente()
    
    try:
        print("\nInforme o código do seu cliente")
        idCliente = int(input("\n=>"))
    except TypeError:
        os.system("clear")
        print("\nInformee apenas numeros inteiros!!")
        return False
    except Exception as error:
        os.system("clear")
        print(f"\nError:{error}")
        return False


    encontrado = list(filter(lambda cliente: cliente[0] == idCliente, lista_clientes))

    if not encontrado:
        os.system("clear")
        print("Esse cliente não existe!!!")
        return False
    
    cliente_sessao = encontrado[0][1]
    return True

def encontrarBanco():
    while True:
        print("0 - Para sair")
        print("INFORME QUAL O SEU BANCO")
        for banco in lista_bancos:
            print(banco[0], " - ", banco[1].nome_banco)
        
        try:
            opcao = int(input("\n=>"))
        except TypeError:
            print("\nInforme apenas numeros inteiros!!")
        except Exception as error:
            print(f"Error: {error}")
            continue
        
        if opcao == 0:
            os.system("clear")
            print("saindo...")
            return None
        
        encontrado = list(filter(lambda banco: banco[0] == opcao, lista_bancos))
        
        if not encontrado:
            os.system("clear")
            print("Banco não foi encontrado!!\n")
            continue

        bancoSelecionado = encontrado[0][1]
        return bancoSelecionado

# Metodo que inclui uma nova conta  
def incluirNovaConta(cliente:Cliente, tipo):

    while True:
        bancoSelecionado = encontrarBanco()
        if bancoSelecionado is None:
            os.system("clear")
            return 0
        
        try:
            agenciaConta = int(input("Informe a agencia: "))
            numeroConta = int(input("Informe o numero da conta: "))
            saldoConta = float(input("Qual o saldo inicial da sua conta: "))
        except Exception as error:
            os.system("clear")
            print("Algo deu errado\n")
            print(f"Error: {error}")
            continue

        if tipo == '1':
            cliConta = ContaCorrente(agenciaConta, numeroConta, saldoConta)
            os.system("clear")
        elif tipo == '2':
            cliConta = ContaPoupanca(agenciaConta, numeroConta, saldoConta)
            os.system("clear")
        else:
            os.system("clear")
            print("Tipo incorreto!!")
            continue
        
        if cliente.conta != None:
            os.system("clear")
            return 0, "Esse cliente já possui uma conta cadastrada!"

        cliente.conta = cliConta
        bancoSelecionado.inserir_cliente(cliente)
        bancoSelecionado.inserir_conta(cliConta)
        
        print("Conta incluida com sucesso!")
        print("Dados da conta:\n")
        print(f"Nome do Cliente: {cliente.nome} {cliente.sobrenome}")
        print(f"Idade do Cliente: {cliente.idade}")
        print(f"Numero do banco: {bancoSelecionado.numero_banco}")
        print(f"Nome do banco: {bancoSelecionado.nome_banco}")
        print(f"Agencia da conta: {cliConta.agencia}")
        print(f"Numero da conta: {cliConta.numero_conta}")
        print(f"Saldo da conta: {cliConta.saldo}")

        print()

        return 0, "Saindo..."




def cadastrarConta():

    if not validaCliente():
        print("Cliente não cadastrado!!!")
        return
    
    while True:
        print("-------------------------------")
        print("      CADASTRO DE CONTA        ")
        print("-------------------------------")

        print("\nTipo de contas:")
        print("\n 1 - Conta Corrente")
        print("\n 2 - Conta Poupança")
        print()
        print(" 0 - sair")

        tipoConta = input("\nInforme o tipo da conta que deseja cadastrar.\n=>")

        if tipoConta not in ('0', '1', '2'):
            print("Informe um tipo valido!")
            continue

        if tipoConta == '0':
            os.system("clear")
            print("saindo do cadastros de contas...")
            return

        elif tipoConta == '1':
            retorno = incluirNovaConta(cliente_sessao, tipoConta)
            if retorno[0] == 0:
                os.system("clear")
                print(retorno[1])
                return

        elif tipoConta == '2':
            retorno = incluirNovaConta(cliente_sessao, tipoConta)
            if retorno[0] == 0:
                os.system("clear")
                print(retorno[1])
                return




def cadastrarCliente():
    global idCliente, lista_clientes
    while True:
        print("-------------------------------")
        print("     CADASTRO DE CLIENTE       ")
        print("-------------------------------")

        try:
            print("Informe o seu primeiro nome(nome)")
            nome = input("=>")
            print()
            print("Informe o seu ultimo nome(sobrenome)")
            sobrenome = input("=>")
            print()
            print("Informe sua idade")
            idade = int(input("=>"))
        except TypeError:
            print("Para idade, informe apenas numeros inteiros")
            continue
        except Exception as error:
            print("Erro não identificado!!")
            print(f"Error: {error}")
            continue
        
        cliente = Cliente(nome, sobrenome, idade)
        lista_clientes.append((idCliente,cliente))
        print(f"\nCliente cadastrado com sucesso!!\nCódigo do Cliente: {idCliente}\nNome do cliente: {nome} {sobrenome}\nIdade: {idade}")
        idCliente+=1
        print()

        continuar = ''
        while continuar not in ("S", "N"):
            continuar = input("Deseja continuar? S/N\n=>").upper()
        
        if continuar == "N":
            os.system("clear")
            print("Saindo...")
            break

def realizarOperacaoConta(banco:Banco, conta:Conta, cliente:Cliente, id_cliente):
    if banco:
        os.system("clear")
    menuOpcoes = """
    1 - Depositar
    2 - Sacar
    
    9 - Entrar em outra conta
    0 - Sair
    """
    while True:
        print("-------------------------------")
        print("         CONTA BANCARIA        ")
        print("-------------------------------")
        print(f"ID cliente: {id_cliente}")
        print(f"Nome cliente: {cliente.nome} {cliente.sobrenome}")
        print(f"Saldo conta: R${conta.saldo:.2f}")
        print("-------------------------------")
        print(menuOpcoes)
        print("-------------------------------")
        print("Informe o que deseja fazer")
        try:
            opcao = int(input("=>"))
        except TypeError:
            os.system("clear")
            print("Informe apenas numeros!")
            continue

        if opcao not in (0,1,2,9):
            os.system("clear")
            print("Opção informada invalida!!")
            continue

        if opcao == 0:
            os.system("clear")
            print("Saindo da conta")
            return False
        if opcao == 9:
            os.system("clear")
            print("Saindo da conta")
            return True

        if opcao == 1:
            os.system("clear")
            try:
                valor_deposito = round(float(input("Qual o valor que deseja Depositar\n=>").replace(",",".")),4)
            except TypeError:
                os.system("clear")
                print("Deve ser informado apenas valorer numericos do tipo Real(float)")
                continue
            except Exception as error:
                os.system("clear")
                print(f"Error: {error}")
                continue

            retorno = banco.realizarDeposito(conta, cliente, valor_deposito)
            if retorno:
                os.system("clear")
                print(retorno)
                continue
            else:
                os.system("clear")
                print("Algo deu errado na operação!!")
                continue
        if opcao == 2:
            os.system("clear")
            try:
                valor_saque = round(float(input("Qual o valor que deseja Sacar\n=>").replace(",",".")),4)
            except TypeError:
                os.system("clear")
                print("Deve ser informado apenas valores numericos do tipo Real(float)")
                continue
            except Exception as error:
                os.system("clear")
                print(f"Error: {error}")
                continue

            retorno = banco.realizarSaque(conta, cliente, valor_saque)
            if retorno:
                os.system("clear")
                print(retorno)
                continue
            else:
                os.system("clear")
                print("Algo deu errado na operação!!")
                continue

            
            








def entrarNaConta():

    global lista_clientes
    while True:
        print("-------------------------------")
        print("         ACESSAR CONTA         ")
        print("-------------------------------")

        print()
        try:
            print("Informe o ID do seu cliente")
            aux_id_cliente = int(input("=>"))
            print("Informe o numero da conta")
            aux_numero_conta = int(input("=>"))
        except TypeError:
            os.system("clear")
            print("Informe apenas numeros")
            continue
        except Exception as error:
            os.system("clear")
            print(f"Error: {error}")
            continue

        encontrado = list(filter(lambda cliente: cliente[0] == aux_id_cliente, lista_clientes))

        if not encontrado:
            os.system("clear")
            print("Cliente não encontrado!")
            continue

        aux_cliente = encontrado[0][1]
        aux_conta = aux_cliente.conta

        if aux_numero_conta != aux_conta.numero_conta:
            os.system("clear")
            print("Conta não localizada")
            continue
        
        bancoSelecionado = encontrarBanco()

        if bancoSelecionado == None:
            os.system("clear")
            print("Banco não encontrado!")
            continue
        
        cliente_x_banco = bancoSelecionado.verificar_cliente(aux_cliente)
        conta_x_banco = bancoSelecionado.verificar_conta(aux_conta)

        if not cliente_x_banco:
            os.system("clear")
            print("Cliente não relacionado a este banco!")
            continue

        if not conta_x_banco:
            os.system("clear")
            print("Conta não encontrada para este banco!")
            continue

        retorno = realizarOperacaoConta(bancoSelecionado, aux_conta, aux_cliente, aux_id_cliente)

        if not retorno:
            return
        
        continue



def start():
    while True:
        print(MENU)
        opcao = input("=>")
        if opcao not in ("1","2","3","0"):
            os.system("clear")
            print("Opção não reconhecida tente novamente!!\n")
            continue

        if opcao == "0":
            os.system("clear")
            print("Muito Obrigado pela preferencia!!!\nAté a proxima!!")
            break

        if opcao == "1":
            os.system("clear")
            cadastrarCliente()
        
        if opcao == "2":
            os.system("clear")
            cadastrarConta()

        if opcao == "3":
            os.system("clear")
            entrarNaConta()

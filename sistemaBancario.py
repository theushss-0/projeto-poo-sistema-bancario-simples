import os

from cliente import Cliente


from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

from banco import Banco

cliente_sessao = 0
idCliente = 0
lista_clientes = []
lista_bancos = [(999, Banco(999,"CAIXA"))]

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
    opcao = input("\n=>")
    
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

# Metodo que inclui uma nova conta  
def incluirNovaConta(cliente:Cliente, tipo):
    opcao = ''
    print("")
    while True:
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

        encontrado = list(filter(lambda banco: banco[0] == opcao, lista_bancos))
        
        if not encontrado:
            os.system("clear")
            print("Banco não foi encontrado!!\n")
            continue

        bancoSelecionado = encontrado[0][1]
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
            os.sytem("clear")
            print("Tipo incorreto!!")
            continue

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

        print("Deseja cadastrar uma nova conta ? S/N")
        sair = input("=>").upper()

        if sair == 'S':
            os.system("clear")
            continue
        else:
            return 0




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
            if retorno == 0:
                os.system("clear")
                return

        elif tipoConta == '2':
            retorno = incluirNovaConta(cliente_sessao, tipoConta)
            if retorno == 0:
                os.system("clear")
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

        

def entrarNaConta():
    while True:
        print("-------------------------------")
        print("         ACESSAR CONTA         ")
        print("-------------------------------")

        print()
        try:
            print("Informe o ID do seu cliente")
            aux_cliente = int(input("=>"))
            print("Informe o numero do banco")
            aux_banco = int(input("=>"))
            print("Informe a Agencia")
            aux_agencia = int(input('=>'))
            print("Informe o numero da sua conta")
            aux_numero_conta = int(input("=>"))
        except TypeError:
            os.system("clear")
            print("Informe apenas numeros")
            continue
        except Exception as error:
            os.system("clear")
            print(f"Error: {error}")
            continue
        

        if aux_cliente not in lista_clientes[0]:
            os.system("clear")
            print("cliente não encontrado")
            continue

        encontrado = list(filter(lambda banco: banco[0] == aux_banco, lista_bancos))

        if not encontrado:
            os.system("clear")
            print("Não foi possível localizar o banco informado")
            continue

        bancoSelecionado = encontrado[0][1]


        if aux_agencia not in bancoSelecionado.agencias:
            os.system("clear")
            print("Essa agencia não é deste banco!")
            continue

        if aux_numero_conta not in bancoSelecionado.contas.numero_conta:
            print("Numero da conta não encontrada!")
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

start()
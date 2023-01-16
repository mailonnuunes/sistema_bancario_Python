menu = '''

[d] Depositar
[s] Sacar 
[e] Extrato 
[f] fechar programa

=>'''

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor >0:
            saldo +=valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("a operação falhou! O valor informado é invalido")

    elif opcao == "s":

         valor = float(input("informe o valor do saque: "))
         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saque = numero_saques > LIMITE_SAQUES

         if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
         elif excedeu_limite:
            print("Operação falhou! você excedeu o limite de saques permitidos no dia")
         elif excedeu_saque:
            print("Operação falhou, limite de saques excedido.")

         elif valor> 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques +=1

         else:
            print("Operação falhou!, o numero informado é invalido.")

    elif opcao == "e":
         print("\n========================= Extrato=========================")
         print("não foram realizadas movimentações." if not extrato else extrato)
         print(f"\nSaldo: {saldo:.2f}")
         print("============================================================")

    elif opcao == "f":

        break;

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
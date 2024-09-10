# Sistema bancário

def deposito(saldo,historico_deposito):
        valor_deposito = float(input("Digite o valor que deseja depositar:"))
        if valor_deposito > 0:
            saldo += valor_deposito
            historico_deposito.append(f"Deposito de: R${valor_deposito:.2f}")
            print(f"Foi depositado o valor de R$:{valor_deposito:.2f}")
        else:
            print("Deposite um valor maior que 0.")
            
        return saldo, historico_deposito   

def saque(saldo,historico_saque):
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > saldo:
            print("Limite indisponível")
        elif len(historico_saque) >= 3:
            print("Vc excedeu o limite de saques")
        elif valor_saque > 0 and valor_saque < saldo:
            saldo -= valor_saque
            historico_saque.append(f"Saque de: R${valor_saque:.2f}")
        return saldo,historico_saque


def extrato(saldo,historico_saque, historico_deposito):
        print("\n====EXTRATO===")
        if not historico_deposito and not historico_saque:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in historico_deposito + historico_saque:
                print(movimentacao)
        print("==============")
        
        print(f"Seu saldo é de R${saldo:.2f}")

def conta_bancaria():
    saldo = 0.00
    historico_saque = []
    historico_deposito = []
    
    
    while True:
        print(
        """
        ==================   
        Bem vindos ao Banco Pablo Gomes 🤑
        
        Qual operação deseja executar?

        A: Deposito
        B: Saque
        C: Extrato
        x: Sair
        ==================
        """
)
        operacao = input("Digite a operação desejada: ").upper()

        if operacao in ["A","B","C","X"]:
            if operacao == "A":
                saldo, historico_deposito = deposito(saldo = saldo , historico_deposito = historico_deposito)
            elif operacao =="B":
                 saldo, historico_saque = saque(saldo = saldo, historico_saque = historico_saque)
            elif operacao =="C":
                extrato(saldo,historico_saque, historico_deposito)
            elif operacao == "X":
                print("Volte sempre!")
                break
        else:
            print("Escolha uma das opções abaixo.")
            
conta_bancaria()






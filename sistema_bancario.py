## Simulação de um Sistema Bancario em PYTHON

## O Usuario possui as opções de sacar, extrato  2depositar 
##Para continuar utilizando o sistema apos uma operacao,
## O Usuario tera que digitar 1 para sair do sistema 2
nome= input("Informe o Seu Nome")
opcao= int(input("Informe a Opção"))
continuar=0
contador=0

saldo=float()

while contador !=5  :

    if opcao==1:
        print("O Seu Saldo e:", saldo)
        continuar= int(input("Deseja continuar 1-SIM 2-Não"))
        if(continuar==1):
            print("Digite 1 para Consultar o Extrato 2 Sacar 3Depositar 4 Sair")
            opcao= int(input("Informe a Opção"))





        else: 
            break
        
    if opcao==2:
        valor_sacado= float(input("Informe o valor a ser sacado"))
        if saldo> valor_sacado:
            saldo -= valor_sacado
            print("Saldo:",saldo)
            continuar= int(input("Deseja continuar 1-SIM 2-Não"))
            if continuar==1:
                contador+=1
                print("Digite 1 para Consultar o Extrato 2 Sacar 3Depositar 4 Sair")
                opcao= int(input("Informe a Opção"))


            else:
                break
                

            
            
        else:
            print("Nao foi Possivel Realizar a Operacao")
            contador+=1
            break
            
    if opcao==3:
        valor_deposito= float(input("Informe o Valor A ser Depositado"))
        saldo+=valor_deposito
        print("Saldo:",saldo)
        continuar = int(input("Deseja Continuar 1-Sim 2-Nao"))
        if continuar==1:
            print("Digite 1 para Consultar o Extrato 2 Sacar 3Depositar 4 Sair")

            opcao= int(input("Informe a Opção"))



            contador+=1

        else:

            break
        

    if opcao==4:
        print("Obrigado por Utilizar o nosso Banco")
        contador=5
print("Obrigado por ser nosso  cliente",nome,"Saldo Disponivel:",saldo)





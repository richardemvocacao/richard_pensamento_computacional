"""



"""
###Calculadora Média Dificuldade

historico = []

while True:
    print("\n--- Calculadora media - Python ---")
    print("1. Operações Básicas (+, -, *, /)")
    print("2. Calcular Porcentagem (X% de Y)")
    print("3. Ver Histórico")
    print("0. Sair")
    
    opcao = input("Escolha: ")

    if opcao == '1':
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        op = input("Operação (+, -, *, /): ")
        
        if op == '+': res = n1 + n2
        elif op == '-': res = n1 - n2
        elif op == '*': res = n1 * n2
        elif op == '/': res = n1 / n2 if n2 != 0 else "Erro"
        
        calc = f"{n1} {op} {n2} = {res}"
        print(calc)
        historico.append(calc)

    elif opcao == '2':
        porcentagem = float(input("Porcentagem (%): "))
        valor = float(input("Sobre o valor: "))
        res = (porcentagem / 100) * valor
        calc = f"{porcentagem}% de {valor} = {res}"
        print(calc)
        historico.append(calc)

    elif opcao == '3':
        print("\n-- Histórico --")
        for item in historico:
            print(item)
            
    elif opcao == '0': break
    
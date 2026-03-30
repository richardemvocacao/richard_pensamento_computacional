
print('\nCalculadora - Python')
num_um = input('Digite o primeiro número: ')
num_dois = input('Digite o segundo número (Lembrando que não pode ser zero para divisão): ')
operacao = input('Escolha a operação: 1-> +, 2-> -, 3-> *, 4-> /')


if operacao == '1':
    result = int(num_um) + int(num_dois)  #Soma
    print(f'O resultado da soma é: {result}')

elif operacao == '2':
    result = int(num_um) - int(num_dois)  # Subtração
    print(f'O resultado da subtração é: {result}')

elif operacao == '3':
    result = int(num_um) * int(num_dois) # Multiplicação
    print(f'O resultado da multiplicação é: {result}')
#Crie o código para realizar a divisão, 
elif operacao == '4':
    if int(num_dois) != 0:
        result = int(num_um) / int(num_dois) # Divisão
        print(f'O resultado da divisão é: {result}')
    else:
        print("Erro: Divisão por zero não é permitida.") ##lembrando de tratar o caso de divisão por zero.
else:
    print("Número não é válido, tente novamente!") 
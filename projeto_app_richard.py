'''

CRUD

salão de beleza

nosso sistema de agendamento online facilita a sua vida: voce escolhe o serviço
o profissional 



'''

print('')

input('pressione enter para sair...')

nome_grande = input(' qual é o seu nome`?:` ')

print(f'olá, {nome_grande}! Seja bem vindo(a) ao nosso salão de beleza!')

print("\n== GESTÃO DO SALÃO ===")
print("1. Agendar Cliente")
print("2. Ver Agenda")
print("3. Mudar Serviço")
print("4. Cancelar Agendamento")
print("5. Relatorio de Serviços")
print("0. Sair")

while True:

    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':

        print("Cadastar cliente...")
        nome_cliente = input("Digite o nome do Cliente: ")
        cliente_telefone = input("Digite o telefone do cliente: ")
        
        print("Cadastro concluido com sucesso\n")

    elif escolha == '2':

        print("mostrar os horarios cadastrados")
        horario_cliente = input("Escolha um horario: ")
        periodo_cliente = input("Escolha o periodo: ")

        print("Horario Cadastrado com sucesso\n")

    if escolha == '3':

        print("Alterar serviço do cliente")
        servico_cliente = input(" digite o novo serviço (corte / barba / Corte + Barba): ")
        print("Serviço alterado com sucesso!")
    
    elif escolha == '4':

        print("cancelar agendamento")
        cliente = input("digite o nome do cliente para cancelar o agendamento: ") 
        horario = input("digite o horario do agendamento para cancelar: ") 
        print("cancelamento com sucesso!")
        
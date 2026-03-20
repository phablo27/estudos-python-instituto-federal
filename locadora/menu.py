import GerenciadorLocacoes

def menu():
    gerenciador = GerenciadorLocacoes()
    
    while True:
        print()
        print()
        print()
        print()
        print()
        print()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                placa = input("Placa do Carro: ")
                cpf = input("CPF do Cliente: ")
                dt_ret = input("Data retirada (DD/MM/AAAA)")
                dt_ent = input("Data entregue (DD/MM/AAAA)")

                nova_locacao = Locacao(placa, cpf, dt_ret, dt_ent, )
            
from calculos import calcular_imposto, calcular_inss

class Banco:
    def __init__(self,titular, numero, agencia, saldo_incial):
        self.titular = titular
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo_incial
        self.historico = []
        
    def registrar_operacao(self, tipo, valor):
        self.historico.append(f'{tipo}: R${valor:.2f}')
        
    def sacar(self, valor_saque):
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f'======= Saque de R$ {valor_saque:.2f} realizado com sucesso! =======')
        else:
            print('Saldo insuficiente!')

    def depositar_salario(self, valor_bruto):
        imposto = calcular_imposto(valor_bruto)
        inss = calcular_inss(valor_bruto)
        descontos = imposto + inss 

        valor_liquido = valor_bruto - descontos
        self.saldo += valor_liquido

        print(f'======= Salário processado para {self.titular}: =======')
        print(f'* Líquido: R${valor_liquido:.2f}')
        print('====================================================')
        print(f'IRPF: R${imposto:.2f} INSS: R${inss:.2f}')
        print('====================================================')

    def exibir_extrato(self):
        print(f'=== EXTRATO DETALHADO - {self.titular} ===')
        for transacao in self.historico:
            print(transacao)
        print(f'Saldo Final: R${self.saldo:.2f}')


#Criação do objeto(instância)
minha_conta = Banco ('Phablo', 123, '001', 0)

#Chamando método de depósito de salário
minha_conta.depositar_salario(12000)

#Chamando método de saque
minha_conta.sacar(50)
minha_conta.sacar(1000)

#Valor final na conta
minha_conta.exibir_extrato()
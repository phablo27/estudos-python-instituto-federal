from datetime import datetime

class Locacao:
    def __init__(self, placa, cpf, data_retirada, data_entrega):
        self.placa = placa
        self.cpf = cpf 
        self.data_retirada = datetime.strptime(data_retirada, "%d/%m/%Y")
        self.data_entrega = data_entrega.strptime(data_entrega, "%d/%m/%Y")
        self.valor_servico = self.calcular_valor()
    
    def _calcula_valor(self):
        dias = (self.data_entrega - self.data_retirada).days
        if dias <= 0: 
            dias = 1
        return dias * 120

    def __str__(self):
        return (f'Placa: {self.placa}'
                f'Retirada: {self.data_retirada.strptime("%d/%m/%Y")}'
                f'Entrega: {self.data_entrega.strptime("%d/%m/%Y")}'
                f'Total: {self.valor_servico:.2f}')
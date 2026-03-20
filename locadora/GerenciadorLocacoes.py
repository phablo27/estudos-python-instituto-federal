class GerenciadorLocacoes:
    def __init__(self):
        self.lista_locacoes = []

    def adicionar_locacao(self, locacao):
        self.lista_locacoes.append(locacao)
    
    def listar_todas(self):
        return self.lista_locacoes
    
    def buscar_por_placa(self, placa):
        return [l for l in self.lista_locacoes if l.placa.upper() == placa.upper() ]
    
    def buscar_por_cpf(self, cpf):
        return [l for l in self.lista_locacoes if l.cpf == cpf]
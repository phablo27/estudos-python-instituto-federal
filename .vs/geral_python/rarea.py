class Empresa:
    def __init__(self, nome, cnpj, endereco, servico):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.servico = servico

    def mostrar(self):
        print("Empresa:")
        print("Nome:", self.nome)
        print("CNPJ:", self.cnpj)
        print("Endereço:", self.endereco)
        print("Serviço:", self.servico)
        print()


class Remedio:
    def __init__(self, nome, tarja, valor, laboratorio, estoque):
        self.nome = nome
        self.tarja = tarja
        self.valor = valor
        self.laboratorio = laboratorio
        self.estoque = estoque

    def mostrar(self):
        print("Remédio:")
        print("Nome:", self.nome)
        print("Tarja:", self.tarja)
        print("Valor:", self.valor)
        print("Laboratório:", self.laboratorio)
        print("Estoque:", self.estoque)
        print()


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, salario, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    def mostrar(self):
        print("Funcionário:")
        print("Nome:", self.nome)
        print("Sobrenome:", self.sobrenome)
        print("CPF:", self.cpf)
        print("Salário:", self.salario)
        print("Cargo:", self.cargo)
        print()


class Livro:
    def __init__(self, titulo, isbn, valor, autor, editora, estoque):
        self.titulo = titulo
        self.isbn = isbn
        self.valor = valor
        self.autor = autor
        self.editora = editora
        self.estoque = estoque

    def mostrar(self):
        print("Livro:")
        print("Título:", self.titulo)
        print("ISBN:", self.isbn)
        print("Valor:", self.valor)
        print("Autor:", self.autor)
        print("Editora:", self.editora)
        print("Estoque:", self.estoque)
        print()


# Instanciando objetos

e1 = Empresa("TechRS", "12345678000100", "Porto Alegre", "TI")
e2 = Empresa("DataSul", "22345678000100", "Canoas", "Dados")
e3 = Empresa("WebDev", "32345678000100", "Gravataí", "Software")

r1 = Remedio("Paracetamol", "Sem Tarja", 10.5, "EMS", 50)
r2 = Remedio("Ibuprofeno", "Sem Tarja", 15.0, "Medley", 40)
r3 = Remedio("Amoxicilina", "Tarja Vermelha", 25.0, "NeoQuimica", 30)

f1 = Funcionario("João", "Silva", "11111111111", 3000, "Analista")
f2 = Funcionario("Maria", "Souza", "22222222222", 3500, "Desenvolvedora")
f3 = Funcionario("Carlos", "Oliveira", "33333333333", 4000, "Gerente")

l1 = Livro("Python Básico", "12345", 80, "José Santos", "TechBooks", 10)
l2 = Livro("POO na Prática", "67890", 90, "Ana Lima", "DevBooks", 15)
l3 = Livro("Banco de Dados", "54321", 100, "Carlos Mendes", "DataBooks", 8)

# Mostrando os dados

e1.mostrar()
e2.mostrar()
e3.mostrar()

r1.mostrar()
r2.mostrar()
r3.mostrar()

f1.mostrar()
f2.mostrar()
f3.mostrar()

l1.mostrar()
l2.mostrar()
l3.mostrar()
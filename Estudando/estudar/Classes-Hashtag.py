# OPP

class Pessoa:
    def __init__(self, nome, cpf, sexo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

if __name__=='__main__':
    pessoa1 = Pessoa('bia', '16646401433', 'F')
    print(pessoa1.nome) 
# Ao criar uma classe estamos trazendo um objeto do mundo para a programação
# Criamos a classe de um objeto que quisermos e dizemos seus atributos e o que eles fazem(métodos).

class Porta:
    def __init__(self, cor, material, tamanho):

        # Atributos da porta

        self.cor = cor
        self.material = material
        self.tamanho = tamanho

        # Métodos da porta
        

porta1 = Porta('azul','ferro','3.0m')

print(porta1.cor)


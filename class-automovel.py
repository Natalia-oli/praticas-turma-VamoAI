class Automovel:
    def __init__(self, tipo, modelo, ano, quilometragem):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def exibir(self):
        print('f{self.tipo}, {self.modelo}, {self.ano}, {self.quilometragem}')

class Carro(Automovel):

    def __init__(self, tipo, modelo, ano, quilometragem):
        super().__init__(tipo, modelo, ano, quilometragem)
    
        
class Moto(Automovel):

    def __init__(self, tipo, modelo, ano, quilometragem):
        super().__init__(tipo, modelo, ano, quilometragem)
    

class PilhaFeira:
    def __init__(self):
        self.feira = []
    
    def push(self, item):
        self.feira.append(item)

    def pop(self):
        if tamanho() == 0:
            return None
        else:
            return self.feira.pop()
        
        def tamanho(self):
            return len(self.feira)


Feira = PilhaFeira()

print(Feira.feira)

Feira.push("kg de Arroz")

Feira.push("kg de Feijao")

print(Feira.feira)



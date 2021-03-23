

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

        def __repr__(self):
            return "{}/n  {}".format(self.nome, self.endereco)

def main():
    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("Hortifruti", Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")

    lista = ListaLigada()
    print(lista.quantidade)

main()
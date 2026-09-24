class Pessoa : 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
            return f"Olá, sou o {self.nome}."
    def aniversario(self):
        self.idade += 1
pessoa1 = Pessoa("Matheus", 23)
print(pessoa1.cumprimentar())
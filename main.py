# Personagem: Classe mãe
# Heroi: Controlado pelo Usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}\n"


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}Habilidade: {self.get_habilidade()}\n"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo, magia):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        self.__magia = magia

    def get_tipo(self):
        return self.__tipo

    def get_magia(self):
        return self.__magia

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}Magia: {self.get_magia()}\nTipo: {self.get_tipo()}\n"


heroi = Heroi(nome="heroi", vida=100, nivel=5, habilidade="super força")
print(heroi.exibir_detalhes())

inimigo1 = Inimigo(nome="Vagante Branco", vida=110, nivel=6, tipo="Morto vivo", magia="Espada de gelo")
print(inimigo1.exibir_detalhes())
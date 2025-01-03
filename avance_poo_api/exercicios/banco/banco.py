# Com base no que vimos nessa aula sobre herança, crie uma classe Banco com dois atributos: nome e endereco. Ambas as classes devem ter apenas o construtor.

class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco
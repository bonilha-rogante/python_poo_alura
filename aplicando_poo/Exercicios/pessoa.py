class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        
    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Profissão: {self._profissao}'
    
    def aniversario(self):
        self._idade += 1
        
    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, eu sou {self._profissao}'
        else:
            return f'Olá, meu nome é {self._nome}'
        
    
pessoa = Pessoa('Guilherme', 32, 'Programador')

print(pessoa)
pessoa.aniversario()
print(pessoa.saudacao)

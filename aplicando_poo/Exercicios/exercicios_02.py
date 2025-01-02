    # Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
    
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
carro_1 = Carro('Fusca', 'Azul', 1975)
        
    
    # Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
    
    # Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
    
    # Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    
class Restaurante:
    def __init__(self, nome, categoria, localidade, ano, ativo = False,):
        self.nome = nome
        self.categoria = categoria
        self.localidade = localidade
        self.ano = ano
        self.ativo = ativo
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante = Restaurante('Cosi', 'Italiano', 'Rua das ruas', 2000)
        


    # Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
    
class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
    

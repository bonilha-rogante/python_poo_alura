    # Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

    # Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
    
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self._qtd_portas = qtd_portas
        
    def __str__(self):
        return super().__str__() + f' | Portas: {self._qtd_portas}'
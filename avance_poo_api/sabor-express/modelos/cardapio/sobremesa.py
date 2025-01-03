from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return f'Nome: {self._nome} | Preço: R$ {self._preco} | Tamanho: {self.tamanho} | Tipo: {self.tipo} | Descrição: {self.descricao}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melância', 5.00, 'Grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pãozinho da cidade')
sobremesa = Sobremesa('Pudim', 13.00, 'Caseiro', 'Individual', 'Pudim caseiro')

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
sobremesa.aplicar_desconto()



restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa)
restaurante_praca.exibir_cardapio


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
    # Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
    
    # Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
    
    # Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
    
    # Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
    
    # Altere o valor do atributo nome para 'Bistrô'.
    
    # Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
    
    # Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
    
    # Mude o estado da instância restaurante_pizza para ativo.
    
    # Imprima no console o nome e a categoria da instância restaurante_praca.
    
    
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurantes)
# print(dir(restaurante_praca))
# print(vars(restaurante_praca))
print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print(f'O restaurante {restaurante_praca.nome} está ATIVO')
else:
    print(f'O restaurante {restaurante_praca.nome} está DESATIVADO')
    
categoria = restaurante_praca.categoria
print(categoria)

restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food')
else:
    print('A categoria não é Fast Food')
    
print(restaurante_pizza.categoria)
restaurante_pizza.ativo = True

print(restaurante_pizza)
print(f'{restaurante_praca.nome} | {restaurante_praca.categoria}')
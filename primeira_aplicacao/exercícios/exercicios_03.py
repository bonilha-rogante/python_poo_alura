# Exercícios

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:

#     Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#     Adicione um campo de profissão para essa pessoa;
#     Remova um item do dicionário.

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

pessoa = {'nome': 'Guilherme', 'idade': 32, 'cidade': 'São Paulo'}

pessoa.update({'nome': 'OK'})
pessoa.update({'profissao': 'Programador'})
pessoa.pop('idade')
print(pessoa)

numero_quadrado = {x: x**2 for x in range(1,6)}
print(numero_quadrado)

if 'profissao' in pessoa:
    print('Existe esse campo')
else:
    print('Não existe esse campo')
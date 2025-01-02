#  Crie uma lista para cada informação a seguir:

#     Lista de números de 1 a 10;
#     Lista com quatro nomes;
#     Lista com o ano que você nasceu e o ano atual.

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['nome1', 'nome2', 'nome3']
anos = [1900, 2024]
soma = 0
for numero in numeros:
    print(numero)
    
for numero in numeros:
    if numero % 2 == 1:
        soma += numero
print(soma)

for i in range(10, 0, -1):
    print(i)
    
tabuada = int(input('Digite um número: '))

for i in range(1, 11):
    valor = tabuada * i
    print(f'{tabuada} X {i} = {valor}')

soma_total = 0
try:
    for numero in numeros:
        soma_total += numero
        print(soma_total)
except Exception as e:
    print(f'Ocorreu um erro: {e}')
   
soma_media = 0 
try:
    for numero in numeros:
        soma_media += numero 
        media = soma_media / len(numeros)
        print(media)

except ZeroDivisionError:
    print(f'Não é possível dividir por zero')

except Exception as e:
    print(f'Ocorreu um erro {e}')
        
import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizzaria', 'ativo':True},
                {'nome':'Cantina', 'categoria': 'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal\n')
    main() 

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo))
    print(linha)
    print(subtitulo)
    print(linha)
    print()
    
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_restaurante = input('Digite o nome do resturante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastro com sucesso!')
    menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    #Para entrar na condicional precisa ser verdadeiro, ou seja a variável precisava ser true, então dessa forma ele está invertendo o valor e caso seja False, ele acessa a mensagem
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    menu_principal()
    
def opcao_invalida():
    exibir_subtitulo('Opção inválida!\n')
    menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print(f'Você escolheu a opção {opcao_escolhida}')
        
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
            

    # if opcao_escolhida == 1:
    #     print('Cadastrar restaurante')
    # elif opcao_escolhida == 2:
    #     print('Listar restaurante')
    # elif opcao_escolhida == 3:
    #     print('Ativar restaurante')
    # else:
    #     finalizar_app()

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
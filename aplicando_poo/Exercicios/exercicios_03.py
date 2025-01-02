    # Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
    
    # Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    
    # Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    
    # Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
    
    # Crie uma instância da classe e imprima o valor da propriedade titular.
    
class ContaBancaria:
    def __init__(self, titular, saldo, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo
        
    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R${self._saldo} | Status: {self._ativo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
        
    @property
    def exibir_status(self):
        return 'Conta ativa' if self._ativo else 'Conta desativada'


conta_1 = ContaBancaria('Guilherme', 1000)
conta_2 = ContaBancaria('Fernanda', 2000)

ContaBancaria.ativar_conta(conta_1)

print(conta_1)



    # Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBando:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao
        
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

    # Crie um método de classe para a conta ClienteBanco.

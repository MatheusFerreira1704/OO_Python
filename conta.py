class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Criando obj{self}")
        # Para "esconder" os atributos no python, utilizamos dois underscore __, no python não se encapsula
        # porém dificulta o acesso e informa ao dev que o atributo não deve ser acessado diretamente.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f"Seu saldo é: {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor <= (self.__saldo + self.__limite)
        
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor de saque não permitido. Você passou do limite para este saque.")

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @staticmethod
    def codigo_bancos():
        return {
                'BB': '001',
                'Caixa': '104', 
                'Bradesco': '237'
                }
        
    @staticmethod
    def codigo_banco():
        return "001"
    
    @property    
    def numero(self):
        return self.__numero
    
    @property    
    def titular(self):
        return self.__titular.title()
    
    @property    
    def saldo(self):
        return self.__saldo
    
    @property    
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    
    
    
    


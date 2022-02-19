class conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = '001'

    def extrato(self):
        print('Saldo {} do titular {}' .format(self.__saldo, self.__titular))

    def deposita(self, valorDeposito):
        self.__saldo = self.__saldo + valorDeposito

    def __pode_sacar(self, saque):
        return saque <= (self.__saldo + self.__limite)

    def saque(self, saque):
        if self.__pode_sacar(saque):
            self.__saldo = self.__saldo - saque
        else:
            print('O valor passou do limite')

    def transferir(self, valor, conta_para_depositar):
        self.saque(valor)
        conta_para_depositar.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

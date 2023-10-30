class Conta:

    def __init__(self, numero, titular, saldo, limite) -> None:
        # print("Construindo o objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo o titular {} é de {} e o limite disponível é de {}".format(
            self.__titular, self.__saldo, self.__limite))

    def depositar(self, valor):
        if (valor > 0):
            self.__saldo += valor
        else:
            print("Valor inválido para depósito")

    def sacar(self, valor):
        if (self.pode_sacar(valor)):
            self.__saldo -= valor
            print("Valor {} sacado com sucesso!".format(valor))
        else:
            print(
                "Saque não realizado, pois o valor desejado é maior que o saldo em conta e o limite disponível.")

    def pode_sacar(self, valor_para_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_para_sacar <= valor_disponivel_para_sacar

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

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

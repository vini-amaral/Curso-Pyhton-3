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
        print("Você está tentando sacar {}".format(valor))

        if (self.__saldo >= valor):
            self.__saldo -= valor
            print("Valor {} sacado com sucesso!".format(valor))
        elif (self.__saldo + self.__limite >= valor):
            print(
                "O valor em conta é insuficiente para realizar o saque. Deseja utilizar o limite?")
            usar_limite = int(input("Digite (1) para SIM e (2) para NÃO: "))
            print(usar_limite)
            if (usar_limite == 1):
                self.__limite -= (valor - self.__saldo)
                self.__saldo = 0
                print("Valor {} sacado com sucesso!".format(valor))
        else:
            print(
                "O valor desejado é maior que o saldo em conta e o limite disponível.\nSaque não realizado.")

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

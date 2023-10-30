from conta import Conta

conta1 = Conta(123, "Ana", 60.0, 500.0)
conta2 = Conta(456, "Bia", 30.0, 500.0)

conta1.extrato()
conta2.extrato()

conta1.transferir(15, conta2)

conta1.extrato()
conta2.extrato()


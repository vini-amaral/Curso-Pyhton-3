from conta import Conta

conta1 = Conta(123, "Ana", 60.0, 500.0)
conta2 = Conta(456, "Bia", 30.0, 500.0)


print(conta1.limite)
conta1.limite = 900.0

print(conta1.limite)

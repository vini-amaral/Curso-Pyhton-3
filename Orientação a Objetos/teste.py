from conta import Conta

conta1 = Conta(123, "Ana", 50.0, 500.0)
print(conta1.codigo_banco())

print(Conta.codigos_bancos())
print(Conta.codigos_bancos()["BB"])
print(Conta.codigos_bancos()["Caixa"])
print(Conta.codigos_bancos()["Bradesco"])

# conta1.sacar(50)

# conta1.sacar(350)

# conta1.sacar(150)

# conta1.sacar(500)

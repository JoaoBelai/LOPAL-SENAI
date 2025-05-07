def troco(valor_conta, valor_pago):
    if valor_pago >= valor_conta:
        troco = valor_pago - valor_conta
        print(f"\nO troco será de: R${troco:.2f}")
    else:
        troco = 0
        print(f"\nR${troco:.2f}"
              f"\nPagamento insuficiente")

valor_conta = float(input("Digite o valor total da compra: "))
vallor_pago = float(input("Digite o valor pago: "))

troco(valor_conta, vallor_pago)
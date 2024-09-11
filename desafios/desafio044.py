print('========== DESAFIO 044 ==========')
precoNormal = float(input('Informe o valor das compras: R$ '))
print('==' * 7, ' MENU ', '==' * 7)
metodoPagamento = int(input("""1 - À vista (dinheiro ou cheque) com 10% de desconto
2 - À vista (no cartão) com 5% de desconto
3 - Em até 2x no cartão com o valor normal
4 - Em 3x ou mais no cartão com 20% de juros
\nInforme o método de pagamento desejado: """))
if metodoPagamento == 1:
    precoDesconto = precoNormal * 0.9
    print('O valor final a ser pago será de R$ {}'.format(precoDesconto))
elif metodoPagamento == 2:
    precoDesconto = precoNormal * 0.95
    print('O valor final a ser pago será de R$ {}'.format(precoDesconto))
elif metodoPagamento == 3:
    print('O valor final a ser pago será de R$ {}'.format(precoNormal))
elif metodoPagamento == 4:
    precoJuros = precoNormal * 1.20
    print('O valor final a ser pago será de R$ {}'.format(precoJuros))
else:
    print('Opção inválida. Tente novamente.')
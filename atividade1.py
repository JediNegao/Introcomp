receita = float(input())
despesas = float(input())
calculo = receita - despesas
calculo2 = despesas - receita

if receita > despesas:
    print("Lucro de R$ {}!".format (calculo))
elif despesas > receita:
    print("Prejuizo de R$ {}!".format (calculo2))



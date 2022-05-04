temperatura = int(input())
if temperatura >= 35 and temperatura <= 70:
    print("Temperatura normal")
if temperatura < 35:
    print("Cheque o hardware")
if temperatura > 70:
    #ele vai verificar a temperatura
    print("Superaquecimento!")
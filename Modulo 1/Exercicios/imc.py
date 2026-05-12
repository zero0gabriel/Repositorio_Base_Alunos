peso = float(input("digite o seu peso em kg: "))
altura = float(input("digite a sua altura: "))

imc = peso / (altura * altura)

if imc >= 30:
    print("cuidado com a sua saude")
else:
    print('tudo ok')

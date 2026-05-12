peso = float(input("digite o seu peso em kg: "))
altura = float(input("digite a sua altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:

    
    print("abaixo do epso")

elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidade grau I")
elif imc <= 39.9:
    print("obesidade grau II")
else:
    print("obesidade grau III(morbida)")

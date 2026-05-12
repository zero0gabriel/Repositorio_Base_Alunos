nota = float(input("Digite a sua nota (notas validas de 0 a 10): "))
while nota < 0 or nota > 10:
    nota = float(input("invalido,digite sua nota entre 0 a 10:"))
print(f"sua nota foi: {nota}")
print = input("digite o nome do aluno:")
nota_01 = int(input("digite a nota 01: ")) 
nota_02 = int(input("digite a nota 02: ")) 
nota_03 = int(input("digite a nota 03: ")) 

media = (nota_01 + nota_02 + nota_03) / 3

if media >= 7:
    print("aprovado.")

elif media > 4:
    print("em recuperacao.")
else:
    print("reprovado.")
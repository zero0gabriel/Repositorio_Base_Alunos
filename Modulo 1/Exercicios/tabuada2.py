numero = int(input("Digite o número da tabuada: ")) 
inicio = int(input("Digite onde a tabuada começa: "))
fim = int(input("Digite até qual número vai a tabuada: "))
while inicio <= fim:
    print(f"{numero} x {inicio} = {numero * inicio}")
    inicio = inicio + 1
# for i in range(inicio, fim + 1):
#     print(f"{numero} X {i} = {numero * i}")

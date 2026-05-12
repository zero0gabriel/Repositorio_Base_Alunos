nome = input("qual e o seu nome: ")
idade = int(input("qual e a sua idade: "))
possui_carteira = input("Possui carteira de motorista? \n (1-Sim / 2-nao)")

if idade >= 18:
    if possui_carteira=="1":
     print("pode dirigir")
    else:
        print("nao pode dirigir")
else:
  print("menor idade")
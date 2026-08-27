import os
import csv

def limpar_tela():
    os.system("cls")

print("Seja bem-vindo ao Sistema de Notas 🤖")

while True:
    opcao = input("[1] - Cadastrar aluno e nota\n" \
    "[2] - Listar alunos\n" \
    "[3] - Listar alunos com nota acima de 8\n" \
    "[0] - Sair\nSua opção: ")

    if opcao == "1":

        nome = input("Digite o nome do(a) aluno(a): ")
        idade = int(input("Digite a idade do(a) aluno(a): "))
        nota = float(input("Digite a nota do(a) aluno(a): "))
        
        with open("alunos.csv","a",newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome,idade,nota])

    elif opcao == "2":
        print("Listar alunos")
    elif opcao == "3":
        print("Listar alunos com nota acima de 8")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
    
    input("Aperte ENTER para continuar")
    limpar_tela()
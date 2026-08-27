def criar_saudacao(nome, periodo):
    if periodo == "manhã":
        return "Bom dia, " + nome
    elif periodo == "tarde":
        return "Boa tarde, " + nome
    else:
        return "Boa noite, " + nome

print(criar_saudacao("Ana", "manhã"))
print(criar_saudacao("lucas", "tarde"))
print(criar_saudacao("maria", "noite"))
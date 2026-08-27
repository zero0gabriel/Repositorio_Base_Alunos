def situacao_aluno(media, frequencia):
    if frequencia < 75:
        return "reprovado"
    elif media >= 7:
        return "aprovado"
    elif media >= 5:
        return "recuperação"
    else:
        return "reprovado"

print(situacao_aluno(8, 80))
print(situacao_aluno(6, 90))
print(situacao_aluno(9, 60))
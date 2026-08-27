def classificar_idade(idade):
    if idade < 0:
        return "idade inválida"
    elif idade < 12:
        return "criança"
    elif idade < 18:
        return "adolescente"
    elif idade < 60:
        return "adulto"
    else:
        return "idoso"

print(classificar_idade(8))
print(classificar_idade(15))
print(classificar_idade(70))
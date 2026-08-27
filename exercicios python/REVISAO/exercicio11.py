def contar_vogais(texto):
    contador = 0

    for letra in texto:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contador = contador + 1

    return contador

print(contar_vogais("casa"))
print(contar_vogais("python"))
print(contar_vogais("banana"))
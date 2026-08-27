def gerar_tabuada(numero):
    lista = []

    for i in range(1, 11):
        lista.append(numero * i)

    return lista

print(gerar_tabuada(2))
print(gerar_tabuada(5))
print(gerar_tabuada(10))
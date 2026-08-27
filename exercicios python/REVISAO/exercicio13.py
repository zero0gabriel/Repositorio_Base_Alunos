def encontrar_maior(numeros):
    maior = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

    return maior

print(encontrar_maior([2, 8, 3]))
print(encontrar_maior([10, 5, 1]))
print(encontrar_maior([7, 7, 7]))
def aplicar_desconto(preco, percentual):
    desconto = preco * percentual / 100
    preco = preco - desconto
    return preco

print(aplicar_desconto(100, 10))
print(aplicar_desconto(50, 20))
print(aplicar_desconto(80, 5))
def dividir_seguro(a, b):
    try:
        return a / b
    except:
        return None

print(dividir_seguro(10, 2))
print(dividir_seguro(8, 0))
print(dividir_seguro(15, 3))
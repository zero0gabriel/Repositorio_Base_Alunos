def eh_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False

print(eh_bissexto(2024))
print(eh_bissexto(2023))
print(eh_bissexto(2000))
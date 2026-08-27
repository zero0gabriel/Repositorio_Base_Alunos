def somar_ate_n(numero):
    if numero < 1: #Verifica se numero é menor que 1
        return 0
    soma = 0 
    for i in range(1, numero + 1): # Vai do 1 até o numero + 1
        soma = soma + i # Soma os números do intervalo entre 1 e número
    return soma

print((somar_ate_n(10000)))
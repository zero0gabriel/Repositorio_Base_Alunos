def somar(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
             return n1 - n2

def dividir(n1,n2):
        return n1 / n2

def mutiplicar(n1,n2):
        return n1 * n2
        
def calcular(n1,n2,operacao):
        if operacao == "+":
                return somar(n1,n2)
        
        elif operacao == "-":
                  return subtrair(n1,n2)
        
         
        elif operacao == "*":
                  return mutiplicar(n1,n2)
        
        elif operacao == "/":
                  return dividir(n1,n2)
        
        else:
                return "operacao invalida"
programa {
  funcao inicio() {

    inteiro numero
    logico ehPositivo,ehNegativo,ehSete

    escreva("Digite um número: ")
    leia(numero)

    ehPositivo = numero > 0
    ehNegativo = numero < 0
    ehSete = numero == 7

    escreva("Esse número é positivo? ", ehPositivo)
    escreva("\nEsse número é negativo? ", ehNegativo)
    escreva("\nEsse número é 7? ", ehSete)
    
  }
}
 
  

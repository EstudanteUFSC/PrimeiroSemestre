numeroX = int(input("Digite um número inteiro x: "))
numeroY = int(input("Digite um número inteiro positivo ou igual a zero: "))

def quantosDigitos(numero):
    digitos = 2
    if (numero / 10) < 1:
        digitos = 1   
    else: 
        while (numero / 10 ) > 10:
            numero = numero / 10
            digitos = digitos + 1
    return digitos

def transformarEmFloatESomar(numeroX, numeroY):    

    if numeroY >= 0:
        contador = 0
        primeiroDigito = -1
        numeroDeDigitos = quantosDigitos(numeroY)
        numero = numeroY
        mostrarNumero = True

        while contador < numeroDeDigitos:
            if contador == numeroDeDigitos:
                primeiroDigito = numero
            numero = numero // 10
            contador = contador + 1
            if primeiroDigito == 0 and numeroY != 0:
                print("O número Y não pode começar com 0!")
                mostrarNumero = False
        else:
            numeroY = numeroY / (10 ** numeroDeDigitos)
            if numeroX > 0:
                novoNumero = numeroX + numeroY
            else: 
                novoNumero = numeroX - numeroY
            if mostrarNumero:
                print("Seu novo número é: ", novoNumero)
            
    else: 
        print("o número Y precisa ser positivo ou igual a 0!")

#reposta questão 
transformarEmFloatESomar(numeroX, numeroY)
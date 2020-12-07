numeroInt = int(input("Digite um número inteiro: "))

def negativoOuPositivo(numero):
    if numero > 0:
        print("O número é positivo")

    if numero < 0: 
        print("O número é negativo")

    if numero == 0:
        print("O número é igual a 0")
        
def quantosDigitos(numero):
    if numero > 0:
        digitos = 2
        if (numero / 10) < 1:
            digitos = 1   
        else: 
            while (numero / 10 ) > 10:
                numero = numero / 10
                digitos = digitos + 1
    else: 
        digitos = 2
        if (numero / 10) > -1:
            digitos = 1   
        else: 
            while (numero / 10 ) < -10:
                numero = numero / 10
                digitos = digitos + 1
    return digitos

def ultimoDigitoIgualPrimeiro(numero, digitos):
    if numero < 0:
        numero = -numero
    if digitos == 1:
        print("O primeiro e o último digito são iguais")
    else:
        contador = 0
        primeiroDigito = 0
        últimoDigito = 0

        while contador < digitos:
            if contador == 0:
                últimoDigito = numero % 10
            if contador == (digitos - 1):
                primeiroDigito = numero
            numero = numero // 10
            contador = contador + 1
        if últimoDigito == primeiroDigito:
            print("O primeiro e o último digito são iguais")
        else:
            print("O primeiro e o último digito não são iguais")

def possuiDigitosIguais(numero, digitos):
    if numero < 0:
        numero = -numero

    indicadoraDePassagem = False
    numeroAtual = 0
    numeroAnterior = 0

    while digitos > 0:
        numeroAtual = numero % 10
        numeroAnterior = (numero // 10) % 10
        if numeroAtual == numeroAnterior:
            indicadoraDePassagem = True
        numero = numero // 10
        digitos = digitos - 1

    if indicadoraDePassagem: 
        print("O número possui dois digitos consecutivos iguais")
    else:
        print("O número não possui dois digitos consecutivos iguais")

def possuiDigitosDobrados(numero, digitos):
    if numero < 0:
        numero = -numero

    indicadoraDePassagem = False
    numeroAtual = 0
    numeroAnterior = 0

    while digitos > 0:
        numeroAtual = numero % 10
        numeroAnterior = (numero // 10) % 10
        if (numeroAtual * 2) == numeroAnterior:
            indicadoraDePassagem = True
        if (numeroAnterior * 2) == numeroAtual:
            indicadoraDePassagem = True
        numero = numero // 10
        digitos = digitos - 1

    if indicadoraDePassagem: 
        print("O número possui dois digitos consecutivos que um é o dobro do outro")
    else:
        print("O número não possui dois digitos consecutivos que um é o dobro do outro")


#resposta letra A 
negativoOuPositivo(numeroInt)

#respota letra B
numeroDeDigitos = quantosDigitos(numeroInt)
print ("O número tem", numeroDeDigitos, "dígitos") 

#resposta letra C
ultimoDigitoIgualPrimeiro(numeroInt, numeroDeDigitos)

#resposta letra D
possuiDigitosIguais(numeroInt, numeroDeDigitos)

#resposta letra E
possuiDigitosDobrados(numeroInt, numeroDeDigitos)
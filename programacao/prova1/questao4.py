def definirQuantidadeNaSequencia():
    quantidadeNaSequencia = int(input("Digite a quantidade de números na seqûencia: "))
    return quantidadeNaSequencia

quantidadeDeInteiros = 0
quantidadeDeFloats = 0

quantidadeNaSequencia = -1

while quantidadeNaSequencia != 0:
    contador = 0
    quantidadeNaSequencia = definirQuantidadeNaSequencia()
    while contador < quantidadeNaSequencia:
        novoNumero = float(input("Digite um número: "))
        if novoNumero < 0:
            novoNumero = -novoNumero
        if novoNumero % 1 != 0:
            quantidadeDeFloats = quantidadeDeFloats + 1
        else: 
            quantidadeDeInteiros = quantidadeDeInteiros + 1
        contador = contador + 1

if quantidadeNaSequencia ==  0:
    print("você digitou", quantidadeDeInteiros, "inteiros e", quantidadeDeFloats, " floats")

#Acredito que minha solução encontrada é confiável sim. Por sempre receber o número como um float
#e conferir se ele é inteiro usando a definição matemática de inteiros (módulo da divisão por 1 ser igual a 0)
#acredito que ele sempre vá retornar a quantidade de inteiros e floats correta. 
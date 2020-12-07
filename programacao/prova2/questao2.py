from questao1 import Matrizes
import random

def inserirMatriz():
    Linhas = int(input("Insira o número de linhas:")) 
    Colunas = int(input("Insira o número de colunas:")) 
    
    matriz = [] 
    print("Insira os números que formarão sua matriz ") 
    
    for i in range(Linhas):
        a = [] 
        for j in range(Colunas):     
            a.append(int(input())) 
        matriz.append(a) 

    return matriz

matriz1 = inserirMatriz()
matriz2 = inserirMatriz()
matriz3 = inserirMatriz()
multiplicador = random.randint(2, 5)

Matrizes(matriz1).lê_matriz()
Matrizes(matriz1).escreve_matriz()
Matrizes(matriz1).soma_matrizes(matriz2)
Matrizes(matriz1).subtrai_matrizes(matriz2)
Matrizes(matriz1).multiplica_matrizes(multiplicador)
Matrizes(matriz1).matrizes_iguais(matriz2, matriz3)
from questao1 import Matrizes

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

matriz = inserirMatriz()

if Matrizes(matriz).quadrado_magico():
    print("Sua matriz é um quadrado mágico!")
else: 
    print("Sua matriz não é um quadrado mágico")

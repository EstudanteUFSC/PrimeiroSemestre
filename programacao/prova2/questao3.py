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

Matrizes(matriz).zeros_nas_matrizes()

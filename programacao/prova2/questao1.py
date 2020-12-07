class Matrizes:
    def __init__ (self, matriz):
        self.matriz = matriz       #Receber a matriz

    def lê_matriz(self):
        return self.matriz
    
    def escreve_matriz(self):
        for i in self.matriz:
            for j in i:
                print(j, end=" ")
            print()

    def soma_matrizes(self, A):
        matrizesLinhas = len(self.matriz)
        matrizesColunas = len(self.matriz[0])
        aLinhas = len(A)
        aColunas = len(A[0])

        if aLinhas == matrizesLinhas and aColunas == matrizesColunas:
            matriz_soma = []
            for i in range(matrizesLinhas):
                matriz_soma.append([])
                for j in range(matrizesColunas):
                    soma = self.matriz[i][j] + A[i][j]
                    matriz_soma[i].append(soma)
            return matriz_soma
        else:
            print("As matrizes precisam possuir o mesmo número de linhas e colunas")

    def subtrai_matrizes(self, A):
        matrizesLinhas = len(self.matriz)
        matrizesColunas = len(self.matriz[0])
        aLinhas = len(A)
        aColunas = len(A[0])

        if aLinhas == matrizesLinhas and aColunas == matrizesColunas:
            matriz_sub = []
            for i in range(matrizesLinhas):
                matriz_sub.append([])
                for j in range(matrizesColunas):
                    soma = self.matriz[i][j] - A[i][j]
                    matriz_sub[i].append(soma)
            return matriz_sub
        else:
            print("As matrizes precisam possuir o mesmo número de linhas e colunas")

    def multiplica_matrizes(self, A):
        matriz_multi = []
        matrizesLinhas = len(self.matriz)
        matrizesColunas = len(self.matriz[0])
        for i in range(matrizesLinhas):
            matriz_multi.append([])
            for j in range(matrizesColunas):
                mult = A * self.matriz[i][j]
                matriz_multi[i].append(mult)
        return matriz_multi

    def matrizes_iguais(self, A, B):
        if self.matriz == A == B:
            return True
        else: 
            return False

    def zeros_nas_matrizes(self):
        matrizesLinhas = len(self.matriz)
        matrizesColunas = len(self.matriz[0])
        linhas = 0
        colunas = 0
        zeros = 0
    
        for i in range(matrizesLinhas): 
            zeros = 0
            for j in range(matrizesColunas):
                if self.matriz[i][j] == 0:
                    zeros = zeros + 1
                
            if zeros == matrizesColunas:
                linhas = linhas + 1

        print("Linhas nulas: ", linhas)
    
        for j in range(matrizesColunas):
            zeros = 0
            for i in range(matrizesLinhas): 
                if self.matriz[i][j] == 0:
                    zeros = zeros + 1

            if zeros == matrizesLinhas:
                colunas = colunas + 1

        print("Colunas nulas: ", colunas)
  
    def quadrado_magico(self): 
        matrizesLinhas = len(self.matriz)
        matrizesColunas = len(self.matriz[0])

        if matrizesLinhas != matrizesLinhas:
            return False

        matrizesLinhas = 3

        diagonalPrincipal = 0 
    
        for i in range(0, matrizesLinhas) : 
            diagonalPrincipal = diagonalPrincipal + self.matriz[i][i] 
    
        diagonalSecundária = 0

        for i in range(0, matrizesLinhas) : 
            diagonalSecundária = diagonalSecundária + self.matriz[i][matrizesLinhas-i-1] 
    
        if (diagonalPrincipal!=diagonalSecundária) : 
            return False
    
        for i in range(0, matrizesLinhas) : 
            somaLinhas = 0;      
            for j in range(0, matrizesLinhas) : 
                somaLinhas += self.matriz[i][j] 
            
            if (somaLinhas != diagonalPrincipal) : 
                return False
    
        for i in range(0, matrizesLinhas): 
            somaColunas = 0
            for j in range(0, matrizesLinhas) : 
                somaColunas += self.matriz[j][i] 
    
            if (diagonalPrincipal != somaColunas) : 
                return False

        return True

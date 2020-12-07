import random

mapaInicial = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

mapaCompleto = [
    [2, 2, 2, 2, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 0],
    [2, 2, 2, 2, 0, 2, 2, 2],
    [0, 0, 0, 2, 2, 2, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 0],
    [2, 2, 2, 0, 0, 2, 2, 0],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2],
]

F = "F" #Fantasma
P = "P" #Pacman

#Deixei o pacman como P e o fantasma como F pra manter apenas um dígito
#e deixar o mapa mais fácil de ler

def printarMapaDoJogo(mapaDoJogo):
    for i in mapaDoJogo:
        for j in i:
            print(j, end=" ")
        print()

def moverPacMan(direção, mapaDoJogo, contador, pacManX, pacManY, casasPercorridas, numeroDeCasas):
    if direção == "d":
        if pacManY < 7 and mapaDoJogo[pacManX][pacManY + 1] != 0:
            if mapaDoJogo[pacManX][pacManY + 1] == 1:
                numeroDeCasas += 1
                casasPercorridas.append(int(str(pacManX) + str(pacManY +1)))
            mapaDoJogo[pacManX][pacManY] = mapaCompleto[pacManX][pacManY]
            mapaDoJogo[pacManX][pacManY + 1] = P
            pacManY = pacManY + 1

            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
        else:
            print(".")
            print("Posição inválida!")
            print("Punição: Você não se moverá na próxima rodada")
            contador = -2
            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
    if direção == "e":
        if pacManY > 0 and mapaDoJogo[pacManX][pacManY - 1] != 0:
            if mapaDoJogo[pacManX][pacManY - 1] == 1:
                numeroDeCasas += 1
                casasPercorridas.append(int(str(pacManX) + str(pacManY - 1)))
            mapaDoJogo[pacManX][pacManY] = mapaCompleto[pacManX][pacManY]
            mapaDoJogo[pacManX][pacManY - 1] = P
            pacManY = pacManY - 1

            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
        else:
            print(".")
            print("Posição inválida!")
            print("Punição: Você não se moverá na próxima rodada")
            contador = -2
            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
    if direção == "c":
        if pacManX > 0 and mapaDoJogo[pacManX - 1][pacManY] != 0:
            if mapaDoJogo[pacManX - 1][pacManY] == 1:
                numeroDeCasas += 1
                casasPercorridas.append(int(str(pacManX - 1) + str(pacManY)))
            mapaDoJogo[pacManX][pacManY] = mapaCompleto[pacManX][pacManY]
            mapaDoJogo[pacManX - 1][pacManY] = P
            pacManX = pacManX - 1

            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
        else:
            print(".")
            print("Posição inválida!")
            print("Punição: Você não se moverá na próxima rodada")
            contador = -2
            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
    if direção == "b":
        if pacManX < 7 and mapaDoJogo[pacManX + 1][pacManY] != 0:
            if mapaDoJogo[pacManX + 1][pacManY] == 1:
                numeroDeCasas += 1
                casasPercorridas.append(int(str(pacManX + 1) + str(pacManY)))
            mapaDoJogo[pacManX][pacManY] = mapaCompleto[pacManX][pacManY]
            mapaDoJogo[pacManX + 1][pacManY] = P
            pacManX = pacManX  + 1

            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
        else:
            print(".")
            print("Posição inválida!")
            print("Punição: Você não se moverá na próxima rodada")
            contador = -2
            return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas
    else:
        print(".")
        print("Tecla inválida!")
        print("Punição: Você não se moverá na próxima rodada")
        contador = -2
        return mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas

def moverFantasma(mapaDoJogo, fantasmaX, fantasmaY, casasPercorridas):
    movimento = random.randint(1, 4)

    if movimento == 1 and fantasmaY < 7: 
        if mapaDoJogo[fantasmaX][fantasmaY + 1] != 0:
            if int(str(fantasmaX) + str(fantasmaY)) in casasPercorridas:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaCompleto[fantasmaX][fantasmaY]
            else:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaInicial[fantasmaX][fantasmaY]
            mapaDoJogo[fantasmaX][fantasmaY + 1] = F
            fantasmaY = fantasmaY + 1

            print(".")
            print("o fantasma andou para direita, cuidado!")
            print(".")
            return mapaDoJogo, fantasmaX, fantasmaY
    if movimento == 2 and fantasmaY > 0: 
        if mapaDoJogo[fantasmaX][fantasmaY - 1] != 0:
            if int(str(fantasmaX) + str(fantasmaY)) in casasPercorridas:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaCompleto[fantasmaX][fantasmaY]
            else:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaInicial[fantasmaX][fantasmaY]
            mapaDoJogo[fantasmaX][fantasmaY - 1] = F
            fantasmaY = fantasmaY - 1

            print(".")
            print("o fantasma andou para esquerda, cuidado!")
            print(".")
            return mapaDoJogo, fantasmaX, fantasmaY
    if movimento == 3 and fantasmaX < 7: 
        if mapaDoJogo[fantasmaX + 1][fantasmaY] != 0:
            if int(str(fantasmaX) + str(fantasmaY)) in casasPercorridas:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaCompleto[fantasmaX][fantasmaY]
            else:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaInicial[fantasmaX][fantasmaY]
            mapaDoJogo[fantasmaX + 1][fantasmaY] = F
            fantasmaX = fantasmaX + 1
            
            print(".")
            print("o fantasma andou para baixo, cuidado!")
            print(".")
            return mapaDoJogo, fantasmaX, fantasmaY
    if movimento == 4 and fantasmaX > 0: 
        if mapaDoJogo[fantasmaX - 1][fantasmaY] != 0:
            if int(str(fantasmaX) + str(fantasmaY)) in casasPercorridas:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaCompleto[fantasmaX][fantasmaY]
            else:
                mapaDoJogo[fantasmaX][fantasmaY] = mapaInicial[fantasmaX][fantasmaY]
            mapaDoJogo[fantasmaX - 1][fantasmaY] = F
            fantasmaX = fantasmaX - 1
            
            print(".")
            print("o fantasma andou para cima, cuidado!")
            print(".")
            return mapaDoJogo, fantasmaX, fantasmaY
def main():

    mapaDoJogo = [
        [P, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, F],
    ]

    contador = 0
    estadoDoJogo = True
    pacManX = 0
    pacManY = 0
    fantasmaX = 7
    fantasmaY = 7
    casasPercorridas = []
    numeroDeCasas = 1
    bemVindo = True

    while estadoDoJogo: 
        if bemVindo: 
            print(".")
            print(".")
            print("Bem vindo ao PacMan")
            print("Percorra todas as casas do mapa e fuja do fantasma para vencer")
            print("As casas marcadas com 0 são paredes e as com 1 são as disponíveis")
            print("As casas já percorridas são marcadas com 2 para facilitar a compreensão")
            print("CUIDADO! Andar em direção a paredes ou bordas do mapa resulta em punição")
            print(".")
            print(".")
            bemVindo = False

        printarMapaDoJogo(mapaDoJogo)

        contador = contador + 1

        if contador >= 0:
            usuárioDeveJogar = True
        else: 
            usuárioDeveJogar = False

        if usuárioDeveJogar:
            print('.')
            direção = input("Pressione d para ir a direita, e para esquerda, c para cima e b para baixo: ")

            resultadoPacMan = moverPacMan(direção, mapaDoJogo, contador, pacManX, pacManY, casasPercorridas, numeroDeCasas)

            if resultadoPacMan is None:
                resultadoPacMan = moverPacMan(direção, mapaDoJogo, contador, pacManX, pacManY, casasPercorridas, numeroDeCasas)

            mapaDoJogo, pacManX, pacManY, contador, casasPercorridas, numeroDeCasas = resultadoPacMan
        
        resultadoFantasma = moverFantasma(mapaDoJogo, fantasmaX, fantasmaY, casasPercorridas)

        while resultadoFantasma is None:
            resultadoFantasma = moverFantasma(mapaDoJogo, fantasmaX, fantasmaY, casasPercorridas)

        mapaDoJogo, fantasmaX, fantasmaY = resultadoFantasma

        if numeroDeCasas == 49:
            print("Parabéns você percorreu todas as casas!")
            estadoDoJogo = False

        if pacManX == fantasmaX and pacManY == fantasmaY:
            print("Você morreu! Tente novamente.")
            estadoDoJogo = False
main()




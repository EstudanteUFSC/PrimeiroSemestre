filha = int(input("Idade da filha: "))
filho = int(input("Idade do filho: ")) 
pai = int(input("Idade do pai: "))
mãe = int(input("Idade da mãe: ")) 

def idadesInversas(idade1, idade2):
    
    segundoDigitoIdade1 = idade1 % 10 
    primeiroDigitoIdade1 = (idade1 - segundoDigitoIdade1) / 10 
    segundoDigitoIdade2 = idade2 % 10 
    primeiroDigitoIdade2 = (idade2 - segundoDigitoIdade2) / 10 
        
    if primeiroDigitoIdade1 == segundoDigitoIdade2 and segundoDigitoIdade1 == primeiroDigitoIdade2:
        return True
    else: 
        return False

if mãe > filha and mãe > filho and pai > filha and pai > filho:
    
    diferencaPaiFilho = pai - filho
    diferencaPaiFilha = pai - filha
    diferencaMaeFilho = mãe - filho
    diferencaMaeFilha = mãe - filha
    
    vezesFilhoInversoPai = 0
    vezesFilhaInversoMae = 0 
    vezesAmbosInversos = 0
    
    if pai > mãe:
        
        diferencaPaiMae = pai - mãe
        
        pai = -1
        mãe = pai - diferencaPaiMae
        filha = pai - diferencaPaiFilha
        filho = pai - diferencaPaiFilho
        
        while mãe < 99: 
            
            pai = pai + 1
            mãe = mãe + 1
            filho = filho + 1
            filha = filha + 1
                                    
            if idadesInversas(pai, filho) and filho > 10:
                vezesFilhoInversoPai = vezesFilhoInversoPai + 1

            if idadesInversas(mãe, filha) and filha > 10: 
                vezesFilhaInversoMae = vezesFilhaInversoMae + 1

            if idadesInversas(pai, filho) and idadesInversas(mãe, filha) and filho > 10 and filha > 10:
                vezesAmbosInversos = vezesAmbosInversos + 1
            
        print("A mãe e a filha tem a idade inversa ", vezesFilhaInversoMae, " vezes")
        print("O pai e o filho tem a idade inversa ", vezesFilhoInversoPai, " vezes")
        print("Ambos tem a idade inversa ", vezesAmbosInversos, " vezes")
        
    else: 
        
        diferencaMaePai = mãe - pai
        
        mãe = -1
        pai = mãe - diferencaMaePai
        filha = mãe - diferencaMaeFilha
        filho = mãe - diferencaMaeFilho
        
        while pai < 99:      
            
            pai = pai + 1
            mãe = mãe + 1
            filho = filho + 1
            filha = filha + 1
            print(pai, filho, mãe, filha)
                        
            if idadesInversas(pai, filho) and filho > 10:
                vezesFilhoInversoPai = vezesFilhoInversoPai + 1

            if idadesInversas(mãe, filha) and filha > 10: 
                vezesFilhaInversoMae = vezesFilhaInversoMae + 1

            if idadesInversas(pai, filho) and idadesInversas(mãe, filha) and filho > 10 and filha > 10:
                vezesAmbosInversos = vezesAmbosInversos + 1
                

        print("A mãe e a filha tem a idade inversa ", vezesFilhaInversoMae, " vezes")
        print("O pai e o filho tem a idade inversa ", vezesFilhoInversoPai, " vezes")
        print("Ambos tem a idade inversa ao mesmo tempo", vezesAmbosInversos, " vezes")

    
else: 
    print("Os filhos não podem ser mais velhos que os pais!")
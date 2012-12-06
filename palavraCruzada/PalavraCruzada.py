'''
Created on 06/12/2012

@author: fernando
'''

def palavraCruzada1( input ):
    
    if len(input.strip()) == 0:
        return True
    
    palavras = input.split()
    
    vertical = palavras[0]
    horizontais = palavras[1:]
    
    index=0
    for palavra in horizontais:
        while index < len(palavra):
            prox_letra = vertical[index]
            if prox_letra not in palavra:
                index+=1 
            else:
                break
        else:
            return False
        
    return True

def palavraCruzada2( input ):

    
    palavras = input.split()

    if len(palavras) <= 1:
        return True
    
    vertical = palavras.pop(0)
    horizontais = palavras
    
    index = 0
    
    for letra in vertical:
        if letra in horizontais[ index ]:
            index+= 1
                    
            if index == len(horizontais):
                return True
            
    return index == len( horizontais )     

def printPalavraCruzada( posicoes, vertical, horizontais):
    
    print
    espacamento_max = max(x2 for _,x2 in posicoes)
    
    index = 0
    for i, letra in enumerate(vertical):
        if index < len(posicoes) and posicoes[index][0] == i:
            espacamento = espacamento_max - posicoes[index][1]
            antes = horizontais[index][:posicoes[index][1]]
            depois = horizontais[index][posicoes[index][1]+1:]
            
            print ' ' * espacamento, antes + letra.upper() + depois 
            index += 1
        else:
            print ' ' * espacamento_max, letra.upper()
        
    pass

def palavraCruzada( input ):

    
    palavras = input.split()

    if len(palavras) <= 1:
        return True
    
    vertical = palavras.pop(0)
    horizontais = palavras
    
    index = 0
    posicoes = []
    for iv,letra in enumerate(vertical):
        if letra in horizontais[ index ]:
            index_letra = horizontais[index].index(letra)
            posicoes.append((iv, index_letra))
            index+= 1
            if index == len(horizontais):
                printPalavraCruzada(posicoes, vertical, horizontais)
                return True
    
    if index == len( horizontais ): 
        printPalavraCruzada(posicoes, vertical, horizontais)       
        return True
    
    return False     
'''
Created on 01/11/2012

@author: DojoNilc
'''
"""
    tokens.append( valor )
"""
import re

def tokenize( input ):
    tokens = [];
    input = input.strip()
    
    if len(input) == 0:
        return []
    
    #split_tokens = re.split("\s+", input)
    split_tokens = re.findall('''
    
    \w+-\w+|      #hyphen
    R\$|US\$|     #Dinheiro
    \d+[\.,]\d+|  #Numero
    \w+|          #Letras
    \W            #Resta
    
    ''', input,re.VERBOSE)
    
    tokens = [ token for token in split_tokens if token!=" " ]

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    input = input.replace("!", " !")
    input = input.replace(". ", " .")
    input = input.replace("?", " ?")
    input = input.replace(",", " ,")
    """    
    #split_tokens = input.split(" ")
    """ 
    for token in split_tokens:
        if token.endswith("!"):
            tokens.append( token.split("!") )
            tokens.append("!")
        else:
            tokens.append( token )
    """        
    
    return tokens

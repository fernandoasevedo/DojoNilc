
def freq( input ):
    saida = ""
    if input != "":
        pontuacao = ['"',',',':','.',';','^','?','!','...']
        tokens = input.split(" ")
        freq_tokens = dict()
        
        for token in tokens:
            token = token.lower()
            if not token in pontuacao:
                """Maneira python"""
                freq_tokens[token] = freq_tokens.get(token,0)+1
                """Maneira tradicional
                if token in freq_tokens.keys():
                    freq_tokens[token] +=1
                else:
                    freq_tokens[token] = 1"""
        
         
        for key in sorted(freq_tokens.keys()):
            saida += key + ":" + str( freq_tokens[ key ] )+" "
            
    
    print saida
        
    return saida
    
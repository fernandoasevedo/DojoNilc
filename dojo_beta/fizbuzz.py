

#saida = saida + ALGUMA_COISA
def fizbuzz2( numeros ):
	saida = ""
	
	#percorrer todos os numeros
	for n in numeros:
		r1 = n % 3
		r2 = n % 5
		
		if r1 == 0 and r2 == 0:
			saida = saida + "fizbuzz "
		elif r1 == 0:
			saida = saida + "fiz "
		elif r2 == 0:
			saida = saida + "buzz "
		else:
			saida = saida + str( n ) + " "
			
	
	return saida
#FIM desta funcao

def fizbuzz( numeros ):
	saida = ""
	
	#percorrer todos os numeros
	for n in numeros:
		r1 = n % 3
		r2 = n % 5
		
		multiplo = False
		
		if r1 == 0:
			saida = saida + "fiz"
			multiplo = True
		
		if r2 == 0:
			saida = saida + "buzz"
			multiplo = True
		
		if not multiplo:		
			saida = saida + str( n )
		
		saida = saida + " "
	
	return saida




numeros = [1, 2, 3]
resposta = "1 2 fiz "
print fizbuzz( numeros ) == resposta

numeros = [1, 2, 4]
resposta = "1 2 4 "
print fizbuzz( numeros ) == resposta

numeros = [1, 2, 3, 5]
resposta = "1 2 fiz buzz "
print fizbuzz( numeros ) == resposta

numeros = [1, 2, 9]
resposta = "1 2 fiz "
print fizbuzz( numeros ) == resposta

numeros = [1, 2, 10]
resposta = "1 2 buzz "
print fizbuzz( numeros ) == resposta

numeros = [1, 2, 15]
resposta = "1 2 fizbuzz "
print fizbuzz( numeros ) == resposta

numeros = [1, 3, 5, 15, 9]
resposta = "1 fiz buzz fizbuzz fiz "
print fizbuzz( numeros ) == resposta

numeros = [3333333]
resposta = "fiz "
print fizbuzz( numeros ) == resposta
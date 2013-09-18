#-*- encoding:utf-8 -*-
'''
Created on 18/09/13

@author: DojoNilc
'''

def check_old (a,b,result,n):
    #n=4
    #digitos que temos
    temos = "".join(sorted(str(a)+str(b)+str(result)))
    todos = "".join(map(str, range(1,n+1)))
    print "temos = ", temos, "todos = ", todos
    return temos == todos


def check (a, b, result,n):
    #n=4
    #digitos que temos
    
    digits = list()
    for digit in str(result):
        digits.append( digit )
        
    digits.append( str(a) )
    digits.append( str(b) )
    s = set( digits )
    #print s
    return len(s) == n and len(digits) == n
    

def pandigital( n ):

    todos ="".join(map(str, range(1,n+1)))
    
    for i in range (1, n+1):
        for j in range(i + 1, n+1):
            result = i * j
            if check(i, j, result, n):
                result_str = str(i) + '*' + str(j) + '=' + str(result)
                return result_str
            
    return ''

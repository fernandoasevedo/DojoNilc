'''
Created on 01/11/2012

@author: DojoNilc
'''

from PalavraCruzada import palavraCruzada
import unittest


class Test(unittest.TestCase):


##    def testeUm(self):
##        
##        resposta = palavraCruzada("")
##        saida = True
##        self.assertEqual( resposta, saida )    
##        
##        pass
##
##    def testeDois(self):
##        
##        resposta = palavraCruzada("hoje dojo escola")
##        saida = True 
##        self.assertEqual( resposta, saida )    
##        
##        pass
##
##    def testeTres(self):
##        
##        resposta = palavraCruzada("hoje dojo nilc")
##        saida = False 
##        self.assertEqual( resposta, saida )    
##        
##        pass
##
##    def testeQuatro(self):
##        
##        resposta = palavraCruzada("hoje")
##        saida = True 
##        self.assertEqual( resposta, saida )    
##        
##        pass
#
#    def testeCinco(self):
#        
#        resposta = palavraCruzada("hojess dojo escola")
#        saida = True 
#        self.assertEqual( resposta, saida )    
#        
#        pass

    def testeSeis(self):
        
        resposta = palavraCruzada("nilc nucleo universidade alegre c")
        saida = True 
        self.assertEqual( resposta, saida )    
        
        pass

unittest.main()
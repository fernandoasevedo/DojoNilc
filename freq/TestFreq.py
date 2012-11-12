#-*- encoding:utf-8 -*- 

"""
Created on 08/11/2012

@author: NilcDojo
"""

import unittest
from Freq import freq

class Test(unittest.TestCase):


    def teste_Um( self ):
        input = ""
        resposta = "";
        self.assertEqual( freq( input ), resposta, "Não passou no teste 1");
    
    def teste_Dois( self ):
        input = "hoje tem dojo"
        resposta = "dojo:1 hoje:1 tem:1 ";
        self.assertEqual( freq( input ), resposta, "Não passou no teste 2");
    
    def teste_Tres( self ):
        input = "hoje tem dojo no nilc , dojo é legal legal"
        resposta = "dojo:2 hoje:1 legal:2 nilc:1 no:1 tem:1 é:1 ";
        self.assertEqual( freq( input ), resposta, "Não passou no teste 3");

    def teste_Quatro( self ):
        input = "Tem hoje Dojo Hoje tem Dojo"
        resposta = "dojo:2 hoje:2 tem:2 ";
        self.assertEqual( freq( input ), resposta, "Não passou no teste 4");
        
    def teste_Cinco( self ):
        input = "Tem hoje Dojo Hoje tem 1 Dojo"
        resposta = "1:1 dojo:2 hoje:2 tem:2 ";
        self.assertEqual( freq( input ), resposta, "Não passou no teste 5");
    
    def teste_Seis( self ):
        input = "Tem hoje Dojo Hoje tem 1 Dojo ..."
        resposta = "1:1 dojo:2 hoje:2 tem:2 ";
        self.assertEqual( freq( input ), resposta, "Não passou no teste 6");
                               
unittest.main()
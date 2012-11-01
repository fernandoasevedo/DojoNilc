#-*- encoding:utf-8 -*- 

'''
Created on 01/11/2012

@author: NilcDojo
'''

import unittest
from Tokenize import tokenize

class Test(unittest.TestCase):


    def teste_Um( self ):
        input = ""
        resposta = [];
        self.assertEqual( tokenize( input ), resposta );
        

    def teste_dois(self):
        input = "hoje tem dojo";
        resposta = ["hoje", "tem", "dojo"];
        self.assertEqual( tokenize( input ), resposta, "Não passou no teste 2");
                

    def teste_Tres( self ):
        input = "     "
        resposta = [];
        self.assertEqual( tokenize( input ), resposta );
        
    def teste_Quatro( self ):
        input = "hoje  tem    dojo"
        resposta = ["hoje", "tem", "dojo"];
        self.assertEqual( tokenize( input ), resposta );       
    
    def teste_Cinco( self ):
        input = "hoje tem dojo!"
        resposta = ["hoje", "tem", "dojo", "!"];
        self.assertEqual( tokenize( input ), resposta );
        
    def teste_Seis( self ):
        input = "hoje tem dojo 1.2"
        resposta = ["hoje", "tem", "dojo", "1.2"];
        self.assertEqual( tokenize( input ), resposta );        
    
    def teste_Sete( self ):
        input = "hoje tem dojo 1.2."
        resposta = ["hoje", "tem", "dojo", "1.2", "."];
        self.assertEqual( tokenize( input ), resposta );    
        
    def teste_Oito( self ):
        input = "hoje tem dojo 11.2."
        resposta = ["hoje", "tem", "dojo", "11.2", "."];
        self.assertEqual( tokenize( input ), resposta );
        
    def teste_Nove( self ):
        input = "A banana custa R$2,50."
        resposta = ["A", "banana", "custa", "R$", "2,50", "."];
        self.assertEqual( tokenize( input ), resposta );
        
    def teste_Dollar( self ):
        input = "A banana custa US$2,50."
        resposta = ["A", "banana", "custa", "US$", "2,50", "."];
        self.assertEqual( tokenize( input ), resposta );
        
    def teste_dez( self ):
        input = "Hoje tem dojo-nilc";
        resposta = ["Hoje", "tem", "dojo-nilc"];
        self.assertEqual( tokenize( input ), resposta );
        
    def teste_arquivo( self ):        
        arquivo = open("input.txt");
        input = arquivo.readline()       
        resposta = ["Hoje", "tem", "dojo-nilc", "."];
        self.assertEqual( tokenize( input ), resposta );
    
        print tokenize( input )
        
        arquivo.close()
        
                       
unittest.main()
#-*- encoding:utf-8 -*-

'''
Created on 18/09/13

@author: DojoNilc
'''

from PandigitalProduct import *
import unittest


class Test (unittest.TestCase):


    def testOneError( self ):
        n = 4
        output = "3*4=12"
        res = pandigital( n )
        self.assertEqual( res, output )
        
        pass

    def testCheck1Error( self ):
        res = check(3, 1, 24 ,4) #temos q ler true
        self.assertEqual( res, True)
        pass
    
    def testCheck2Error( self ):  
        res = check(3, 1, 243, 4) #temos q ler falso
        self.assertEqual( res, False)
        pass
    
    def testCheck3Error( self ): 
        res = check(3, 1, 34, 4) #temos q ler falso
        self.assertEqual( res, False)
        pass
    
#    def testTwoError( self ):
#        n = 5
#        output = "13*4=52"
#        res = pandigital( n )
#        self.assertEqual( res, output )
#        
#        pass
    

unittest.main()

import unittest
from Division import division

#Definisanje test klase
class testDivisionNumbers(unittest.TestCase):
    #Definisanje test slučajeva
    
    # slicaj deljenje sa nulom    
    def test_division_zero(self):
        firstNumber=12
        secondNumber=0
        result=division(firstNumber,secondNumber)
        self.assertRaises(ZeroDivisionError,result,True) 
        
    # Slučaj deljenik je string   
    def test_division_string_deljenik(self):
        firstNumber="String"
        secondNumber=4
        result=division(firstNumber,secondNumber)
        self.assertRaises(TypeError,result,True)
        
    # Slučaj delilac je string   
    def test_division_string_delilac_(self):
        firstNumber=12
        secondNumber="String"
        result=division(firstNumber,secondNumber)
        self.assertRaises(TypeError,result,True)
        
# Definisanje skupa testova
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testDivisionNumbers)) 
    return test_suite

mySuite=suite()

#Definisanje runera

runner=unittest.TextTestRunner()
runner.run(mySuite)        
        
        

        
    
    

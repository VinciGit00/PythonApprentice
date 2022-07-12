from Testing import sum, dif, prod, div, mod
import unittest

class testcase1(unittest.TestCase):
    #Test functions
    def testSum(self):
        self.assertEqual(sum(1,2), 3, "sum not correct")

    def testDif(self):
        self.assertEqual(dif(3,2),1, "dif not correct")

    def testprod(self):
        self.assertEqual(prod(3,2), 6, "prod not correct")

    def testdiv(self):
        self.assertEqual(div(2,1), 2.0, "div not correct")

    def testmod(self):
        self.assertEqual(mod(2,1),0, "mod not correct")
        
#Call the main of the test class
if __name__ == "__main__":
    unittest.main()
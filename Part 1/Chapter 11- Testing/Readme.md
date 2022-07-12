# Chapter 11- Testing

## Testing a function

To test a function you have to create a separate file for the the test and inside it there’s the main function to do the testing.

## File function

```python
def sum(a, b):
    return a+b

def dif(a, b):
    return a-b

def prod(a,b):
    return a*b

def exp(a,b):
    a**b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b
```

## Test class

```python
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
```

### Steps

- Import the class you need
- Import unittest
- Create the test class with the caption unittest.TestCase inside the brackets
- Create the test function with self.asserEqual
- crete the main of the test

```python
if __name__ == "__main__":
    unittest.main()
```

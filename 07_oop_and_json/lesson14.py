x = 5
y = 7
print(f"x: {x}, y: {y}")
result =x + y
print(f"result: {result}")


def add_numbers(a, b):
    
    return a + b
add_numbers(5, 9)


def multiply_numbers(a, b):
   
    return a * b
multiply_numbers(6, 9)


#unittest

import unittest
class TestMathoperations(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3,4), 7)
        self.assertEqual(add_numbers(-1,0), -1)
        self.assertEqual(add_numbers(5,9), 14)
if  __name__ == "__main__":
    unittest.main()
def add_numbers(a, b):
    result = a + b
    return result




x = add_numbers(3, 4)
print(x)


def multiply(a, b):
    result = a * b
    return result



x = multiply(5, 9)
print("Result:", x)

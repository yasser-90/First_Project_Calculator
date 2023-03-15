import math
class opeartion:
    def subtract(x, y):
        return x - y

    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y
    
    def max(x, y):
        return max(x,y)
    
    def min(x, y):
        return min(x,y)
    
    def power(x, y):
        return x**y
    
    def remainder(x, y):
        return x % y

    def underdivided(x, y):
        return x // y

    def sqrt(x):
        return math.sqrt(x)
    
    def sin(x):
        return math.sin(x)
    
    def cos(x):
        return math.cos(x)
    
    def tan(x):
        return math.tan(x)
    
    def factorial(x):
        if x == 0:
            return (0)
        else:
            f=1.0
            for i in range(1, int(x) + 1):
                f = f * i
        return (f)
    

    
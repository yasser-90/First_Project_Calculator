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
    def power(x,y):
        return x ** y
    
    def cosine(x):
        angle_radians = math.radians(x)  #used to convert an angle from degrees to radians.                   بالتقدير الدائري.
        return math.cos(angle_radians)
     
    def sine(x):
        angle_radians = math.radians(x)
        return math.sin(angle_radians)
    
    def tanget(x):
        angle_radians = math.radians(x)
        return math.tan(angle_radians)
     
    def logartim(x):
        return math.log(x)
    
    def pai(x):
        return math.pi*(x)
    
    def Square(x):
        return math.sqrt(x)
    
    def cube_root(x):
        return math.pow(x,1/3)
        
    def max_num(x,y):
        if x > y:
            return x
        else:
            return y
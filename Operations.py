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

    def equation_oper(equ):
        try:
            result = eval(equ)
        except:
            result = None
        return result

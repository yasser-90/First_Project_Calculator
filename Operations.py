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

class operation2:
    def __init__(self):
        pass

    def input(self):
        try:
            result = eval(input("calculate:\n"))
            print("Result = " + str(result))
        except ZeroDivisionError:
            print("can not divided by zero")
        except UnboundLocalError:
            print("no")
        except SyntaxError:
            print("no entry !")
        except NameError:
            print("you must enter numbers and operations!")

import math


class Opeartion:
    # This function sub  multi numbers
    @staticmethod
    def subtract(numbers):
        sub = numbers[0]
        for counter in range(len(numbers)):
            if counter > 0:
                sub -= numbers[counter]
        return sub
    # This function adds two numbers

    @staticmethod
    def add(numbers):
        sum = 0
        for value in numbers:
            sum += value
        return sum

    # This function multiplies two numbers
    @staticmethod
    def multiply(numbers):
        mul = 1
        for value in numbers:
            mul *= value
        return mul

    # This function divides two numbers
    @staticmethod
    def divide(numbers):
        if 0 in numbers and numbers[0] > 0:
            return "Cant divide on zero..."
        else:
            div = numbers[0]
            for counter in range(len(numbers)):
                if counter > 0:
                    div /= numbers[counter]
        return div
    # This function cos

    @staticmethod
    def cos(number):
        return math.cos(number)
    # This function sin

    @staticmethod
    def sin(number):
        return math.sin(number)

    # This function tan

    @staticmethod
    def tan(number):
        return math.tan(number)

    # This function squer

    @staticmethod
    def squer(number):
        return math.sqrt(number)

    # This function factorial
    @staticmethod
    def factoril(number):
        return math.factorial(number)

    # This function power
    @staticmethod
    def power(x, y):
        return x ** y

    # This function remender
    @staticmethod
    def remender(number, div):
        return number % div

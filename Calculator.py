import math
from Operations import opeartion as oper
#  User Select  the operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.cosin")
print("7.sin")
print("8.tan")
print("9.Logarithm")
print("10. πi ")
print("11. √ Sqrt ")
print("12. √ Cube")
print("13.Maximum")
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    # check if choice is one of the options
    if choice in ('1', '2', '3', '4', '5','6','7','8','9','10','11','12','13'):
        # Get user input for operands
        if choice != '6' and choice != '7' and choice != '8' and choice != '9' and choice != '10' and choice != '11' and choice != '12':
            num1 = float(input("Enter first number: "))  # user enter first number (operand)
            num2 = float(input("Enter second number: "))  # user enter second number (operand)
        else:
            num1 = float(input("Enter number: "))

        print("Result of Operation = ")
        if choice == '1':
            print(num1, "+", num2, "=", oper.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", oper.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", oper.multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=",oper.divide(num1, num2))
        
        elif choice == '5':
            print(num1, "^", num2, "=", oper.power(num1, num2))
        
        elif choice == "6":
            print("cosine",num1, "=", oper.cosine(num1))
        
        elif choice == "7":
            print("sine",num1, "=", oper.sine(num1))
        
        elif choice == "8":
            print("tan",num1, "=", oper.tanget(num1))
        
        elif choice == "9":
            print("logarithm of",num1,"=",oper.logartim(num1))
        
        elif choice == "10":
            print("π of ", num1, "=",oper.pai(num1))
        
        elif choice == "11":
            print("√ Sqrt of ",num1,"=",oper.Square(num1))
        
        elif choice == "12":
            print("√ cube root of ",num1 ,"=", oper.cube_root(num1))

        elif choice == "13":
            print("The maximum of", num1, "and", num2, "is = ", oper.max_num(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")